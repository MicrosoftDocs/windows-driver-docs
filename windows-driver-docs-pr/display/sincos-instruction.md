---
title: SINCOS Instruction Format
description: SINCOS Instruction Format
ms.assetid: df9b51ef-5a9f-4222-a0be-a40d5b577f9a
ms.date: 01/05/2018
ms.localizationpriority: medium
---

# SINCOS Instruction Format


## <span id="ddk_sincos_instruction_gg"></span><span id="DDK_SINCOS_INSTRUCTION_GG"></span>


The SINCOS instruction computes sine and cosine, in radians. The X component of the result contains cos(x); the Y component contains sin(x).

### <span id="format"></span><span id="FORMAT"></span>Format

[instruction token](instruction-token.md) that contains D3DSIO\_SINCOS. Instruction length is 4.

[destination parameter token](destination-parameter-token.md) using the D3DSPR\_TEMP [register type](https://msdn.microsoft.com/library/windows/hardware/ff569707).

first [source parameter token](source-parameter-token.md). Requires explicit use of replicate swizzle, that is, the X, Y, Z, or W swizzle component (or the R, G, B, or A equivalent) must be specified.

**The following source tokens are for pixel and vertex shader versions earlier than 3\_0. That is, for pixel and vertex shader version 3\_0 and later, only the first source parameter token is used.**

second source parameter token using the D3DSPR\_TEMP register type.

third source parameter token using the D3DSPR\_TEMP register type.

### <span id="comments"></span><span id="COMMENTS"></span>Comments

The second and third sources could be used as temporary registers.

Source register rules:

-   src1. selected\_channel is an angle measured in radians between -Pi and +Pi.

-   src2 = (âˆ’1.f/(7!\*128), âˆ’1.f/(6!\*64), 1.f/(4!\*16), 1.f/(5!\*32) ).

-   src3 = (âˆ’1.f/(3!\*8), âˆ’1.f/(2!\*8), 1.f, 0.5f).

    The ordering of the last two numbers in src2 and src3 is specifically chosen to accommodate pixel shader 2.0, which also has the SINCOS macro. Reversing these numbers means that the macro expansion can use one of the few custom source swizzles that is available to ps\_2\_0 (vertex shaders have general swizzle so there is no issue). This allows the same custom constants to be used, regardless of where sincos is being used.

Destination register rules:

-   dest.x = cos(src1.selected\_channel), dest.y = sin(src1.selected\_channel), dest.z is undefined after the instruction.

-   dest should not be the same register as src1.

-   Only X and Y are allowed to be in the destination write mask.

The SINCOS instruction is a macro instruction that takes eight instruction slots.

Only X and Y are allowed to be in the destination write mask.

The maximum absolute error is 0.002.

### <span id="operation"></span><span id="OPERATION"></span>Operation

The following shows the Taylor series for sin(x) and cos(x):


`(1) cos(x) = 1 - x2/2! + x4/4! - x6/6!
sin(x) = x - x3/3! + x5/5! - x7/7! = x*(1 - x2/3! + x4/5! - x6/7!)`

To increase precision we compute cos(x) using cos(x/2):

`(2) cos(x) = 1 - 2*sin(x/2)*sin(x/2)
sin(x) = 2*sin(x/2)*cos(x/2)`

(1) can be re-written by substituting x to x/2 as:

`(3) cos(x) = 1 - x2/(2!*4) + x4/(4!*16) - x6/(6!*64)
sin(x) = x/2 - x3/(3!*8) + x5/(5!*32) - x7/(7!*128) =
= x*(0.5f - x2/(3!*8) + x4/(5!*32) - x6/(7!*128))`

Lets, write (3) in vector form. Here a,b,c,d are 2D constant vectors:

`a + x2*b + x4*c + x6*d = a+x2*(b + x2*(c + x2*d)`


The following shows the implementation for SINCOS:


SRC2 should be constant:

`(1.f/(7!*128), 1.f/(6!*64), 1.f/(4!*16), 1.f/(5!*32) )`

SRC3 should be constant:

```cpp
(1.f/(3!*8), 1.f/(2!*8), 1.f, 0.5f )
VECTOR v1 = EvalSource(SRC1);
VECTOR v2 = EvalSource(SRC2);
VECTOR v3 = EvalSource(SRC3);
VECTOR v;
MUL v.z, v1.w, v1.w ; x*x
MAD v.xy, v.z, v2.xy, v2.wz
MAD v.xy, v.xy, v.z, v3.xy
MAD v.xy, v.xy, v.z, v3.wz ; 
```

Partial sin(x/2) and final cos(x/2):

```cpp
MUL v.x, v.x, v1.w ; sin(x/2)
MUL v.xy, v.xy, v.x ; compute sin(x/2)*sin(x/2) and sin(x/2)*cos(x/2)
ADD v.xy, v.xy, v.xy ; 2*sin(x/2)*sin(x/2) and 2*sin(x/2)*cos(x/2)
ADD v.x, -v.x, v3.z ; cos(x) and sin(x)
WriteResult(v, DST);
```

If an application must compute SINCOS for an arbitrary angle, the angle can be mapped to the range -Pi...+Pi by using the following macro (r0.x holds the original angle):

```macro
def c0, Pi, 0.5f, 2*Pi, 1/(2*Pi)
mad r0.x, r.x, c0.w, c0.y
frc r0.x, r0.x
mad r0.x, r0.x, c0.z, -c0.x
```

## <span id="Requirements"></span><span id="requirements"></span><span id="REQUIREMENTS"></span>Requirements


Available in Windows Vista and later versions of the Windows operating systems.

 

 





