# Rubiks Toolkit
A solution to learn algorithms and practice for Rubiks Cube Competitions.

## Documentation 
```
/scramble2
```
Generates a 2x2 Scramble
```
/scramble3
```
Generates a 3x3 Scramble
```
/compscrambles
```
Generates 5 Scrambles as per WCA competition rules
```
/compaveragecalc/<t1>/<t2>/<t3>/<t4>/<t5>
```
Calculates the official WCA average of a 5 solve set
```
/allalgs
```
Gets all alternate algorithms 
```
/alt/<algname>
```
Returns alternate algorithms posted by other users for specified PLL ( ie. Ua )
```
POST
curl -X POST "https://rottencalc.pythonanywhere.com/alt/<algname>" \
     -H "Content-Type: application/json" \
     -d '{"alternate_algorithm": "MESSAGE"}'

```
Abiity to Post an alternate algorithm for a specified PLL( ie. Ua ) Be Nice no weird posts please!!!
```
/<algname>
```
Returns the common algorithm for the specified PLL ( ie. Ua )
