import {readFileSync} from 'node:fs';
import vm from 'node:vm';
import assert from 'node:assert/strict';
import {existsSync} from 'node:fs';

const html=readFileSync(new URL('../assets/annotation-review.html',import.meta.url),'utf8');
const core=html.match(/<script id="review-core">([\s\S]*?)<\/script>/)[1];
const {validateProject,defaultProject,normalizedPoint,feedbackFrom}=vm.runInNewContext(core+'\n({validateProject,defaultProject,normalizedPoint,feedbackFrom})');
const p=defaultProject();
p.views.front.image={id:'test-image',name:'test.png',width:1,height:1,sha256:'a'.repeat(64),dataUrl:'data:image/png;base64,AA=='};
p.views.front.annotations=[{id:1,type:'arrow',points:[{x:.25,y:.4},{x:.6,y:.7}],instruction:'Make this strap 20 mm.'}];
p.nextAnnotationId=2;
p.questions=[{id:'trim',question:'Choose trim',options:[1,2,3,4,5].map(id=>({id:String(id),label:'Option '+id})),selectedOptionId:'3',customAnswer:''}];
assert.equal(validateProject(JSON.parse(JSON.stringify(p))).garment.baseRevision,'v1');
const fit=normalizedPoint(160,260,{left:10,top:20,width:600,height:600});
const zoom=normalizedPoint(310,500,{left:10,top:20,width:1200,height:1200});
assert.equal(fit.x,zoom.x);assert.equal(fit.y,zoom.y);
const f=feedbackFrom(p);
assert.equal(f.views.front.image.sha256,p.views.front.image.sha256);
assert.equal('dataUrl' in f.views.front.image,false);
assert.equal(f.views.front.annotations[0].points[1].x,.6);
assert.equal(f.answers[0].answer,'Option 3');
f.views.front.annotations[0].points[0].x=.9;
assert.equal(p.views.front.annotations[0].points[0].x,.25);
for(const mutate of [
 x=>x.views.front.annotations[0].points[0].x=NaN,
 x=>x.views.front.annotations[0].points[0].y=1.1,
 x=>x.views.front.image.dataUrl='https://example.com/private.png',
 x=>x.views.extra={image:null,annotations:[]},
 x=>x.questions[0].options.pop(),
 x=>x.views.front.annotations[0].type='unknown',
 x=>x.views.back.annotations.push({...x.views.front.annotations[0],type:'note',points:[]}),
]){const copy=JSON.parse(JSON.stringify(p));mutate(copy);assert.throws(()=>validateProject(copy));}
for(const match of html.matchAll(/<script(?:\s[^>]*)?>([\s\S]*?)<\/script>/g)){
 if(match[0].includes('application/json'))continue;
 new vm.Script(match[1]);
}
console.log('PASS: zoom coordinates, project round-trip, feedback identity, validation, script syntax.');
const skill=readFileSync(new URL('../SKILL.md',import.meta.url),'utf8');
const frontmatter=skill.match(/^---\r?\n([\s\S]*?)\r?\n---/)[1];
const entries=Object.fromEntries(frontmatter.split(/\r?\n/).map(line=>{const at=line.indexOf(':');return [line.slice(0,at),line.slice(at+1).trim()];}));
assert.equal(entries.name,'streetwear-fashion-design');
assert.equal(Object.keys(entries).sort().join(','),'description,name');
assert.ok(entries.description.length<=1024&&!/[<>]/.test(entries.description));
assert.ok(!skill.includes('[TODO:'));
for(const match of skill.matchAll(/\]\((?!https?:)([^)]+)\)/g))assert.ok(existsSync(new URL('../'+match[1],import.meta.url)),match[1]);
console.log('PASS: skill frontmatter, invocation name, description, and resource links.');
