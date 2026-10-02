import {readFileSync} from 'node:fs';
import vm from 'node:vm';
import assert from 'node:assert/strict';

const html=readFileSync(new URL('../assets/design-explorer.html',import.meta.url),'utf8');
const core=html.match(/<script id="explorer-core">([\s\S]*?)<\/script>/)[1];
const {validateExplorer,defaultExplorer,choicesFrom,selectedViews}=vm.runInNewContext(core+'\n({validateExplorer,defaultExplorer,choicesFrom,selectedViews})');
const p=defaultExplorer(true);
assert.equal(p.answers[0].answer,'Båtutringning');
assert.throws(()=>choicesFrom(p));
p.selectedOptionId='pencil';
const before=JSON.stringify(p);
const f=choicesFrom(p);
assert.equal(f.kind,'fashion-design-choices');
assert.equal(f.garment.id,p.garment.id);
assert.equal(f.garment.baseRevision,p.garment.baseRevision);
assert.equal(f.answers[0].answer,'Båtutringning');
assert.equal(f.answers[1].selectedOptionId,'pencil');
assert.equal(f.needsRedraw,false);
assert.equal(f.conceptStatus,'exploring');
assert.equal(selectedViews(p).front,p.question.options[0].views.front);
f.answers[0].answer='Mutated';f.brief[0].value='Mutated';
assert.equal(JSON.stringify(p),before);
assert.equal(validateExplorer(JSON.parse(before)).selectedOptionId,'pencil');
p.selectedOptionId='custom';
assert.throws(()=>choicesFrom(p));
p.customAnswer='Draw a softer contour while keeping the neckline.';
const custom=choicesFrom(p);
assert.equal(custom.needsRedraw,true);
assert.equal(custom.answers.at(-1).answer,p.customAnswer);
assert.equal(selectedViews(p).front,p.baseViews.front);
for(const mutate of [
 x=>x.question.options.pop(),
 x=>x.question.options[1].id=x.question.options[0].id,
 x=>x.question.category='__proto__',
 x=>x.selectedOptionId='unknown',
 x=>x.answers.push({...x.answers[0]}),
 x=>x.answers[0].id=x.question.id,
 x=>x.question.options[0].views.extra='<svg />',
 x=>x.question.options[0].views.side=x.baseViews.front,
 x=>x.garment.id='',
 x=>x.question.options[0].views.front='https://example.com/image.svg',
]){const copy=JSON.parse(JSON.stringify(p));mutate(copy);assert.throws(()=>validateExplorer(copy));}
for(const match of html.matchAll(/<script(?:\s[^>]*)?>([\s\S]*?)<\/script>/g))if(!match[0].includes('application/json'))new vm.Script(match[1]);
console.log('PASS: explorer identity, prior answers, selections, round-trip, custom redraw, invalid input, syntax.');
