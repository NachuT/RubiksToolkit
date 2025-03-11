# Rubiks Toolkit
A solution to learn algorithms and practice for Rubiks Cube Competitions.

## Documentation 
#Generates a 2x2 Scramble
```
/scramble2
```
# Generates a 3x3 Scramble
```
/scramble3
```
# Generates 5 Scrambles as per WCA competition rules
```
/compscrambles
```
# Calculates the official WCA average of a 5 solve set
```
/compaveragecalc/<t1>/<t2>/<t3>/<t4>/<t5>
```
# Gets all alternate algorithms 
```
/allalgs
```
# Returns alternate algorithms posted by other users for specified PLL ( ie. Ua )
```
/alt/<algname>
```
# Abiity to Post an alternate algorithm for a specified PLL( ie. Ua ) Be Nice no weird posts please!!!
```
POST
curl -X POST "https://rottencalc.pythonanywhere.com/alt/<algname>" \
     -H "Content-Type: application/json" \
     -d '{"alternate_algorithm": "MESSAGE"}'

```
# Returns the common algorithm for the specified PLL ( ie. Ua )
```
/<algname>
```
