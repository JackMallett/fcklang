# fcklang

Variable Declaration

declare variables as

```name = value```

most names with no spaces or math symbols should work although im sure it'll break somewhere I didnt think of

you can print to the stdout using
```say(x)```
expressions within the function will be evaluated

you can get the length of a string or array using
```howbig(x)``` which returns an integer

you can make a loop using
```loop(arg1, arg2, arg3){
    loop body
}
```
where arg1 is evaluated at the beginning of the loop
ex: ```i = 1```

arg2 is evaluated at the start of each loop iteration and will continue when false
ex: ```i < 5```

arg3 is evaluated at the end of each loop iteration
ex: ```i = i + 1```