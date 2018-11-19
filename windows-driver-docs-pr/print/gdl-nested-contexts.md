---
title: GDL Nested Contexts
description: GDL Nested Contexts
ms.assetid: c679937a-fa36-487a-84f2-f61a7ef0198e
keywords:
- GDL WDK , contexts
- contexts WDK GDL , nested contexts
- nested contexts WDL GDL
- GDL WDK , values
- values WDK GDL , nested contexts
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# GDL Nested Contexts


A *nested context* is introduced with the *begin nesting character* (which is an opening parenthesis or an opening square bracket). The nested context ends when the matching *end nesting character* (which is a closing parenthesis or closing square bracket) is encountered.

Nesting contexts can be nested within each other. The end nesting characters can be used only to end the current nesting context. If end nesting characters appear anywhere else, it is a syntax error.

Within a nested context, the [construct delimiter characters](gdl-construct-delimiters.md) lose their meaning as construct delimiters and are also treated as nested context delimiters. Within a nested context, a linebreak sequence is treated as non-literal whitespace.

The nested context can appear outside of any context or within another nested context but not within any other context. Any context, including other nested contexts, can appear within a nested context, except for the HexSubString context.

The following code example shows a GDL nested context.

```cpp
*good_nests: ( { } [ ( ) ] )
```

The following code examples shows GDL nested contexts that contain errors.

```cpp
*bad_nests: (  ] *%  end nesting delimiter can only be used within its nesting context.
*bad_nests: (  ]  )
*bad_nests:   ] [   *%  end nesting delimiter can only be used within its nesting context.
*bad_nests: (  [  )   ]   *%  end nesting delimiter can only be used within its nesting*% context.  In this case the ')' char cannot be used within the context begun 
*%by '[' .
*bad_nests:  {  [ ]  }  *% attempt to use construct delimiter to define a nesting context 
*%  outside of a nesting context.
```

The entire contents of a nested context is treated as part of the [value](gdl-values.md). For example, the following GDL code represents one entry with a keyword of "\*KeywordA". The remainder of the fragment is the value of \*KeywordA, because what appears to be separate entries for \*KeywordB and \*KeywordC are contained within a nested context. In fact, the numbers "12, 38, 709" are themselves in a nested context that is defined by parentheses delimiters that are nested within the outer context that is defined by the square bracket delimiters.

```cpp
*KeywordA: [
*KeywordB:  List(12, 38, 709)
*KeywordC:  "the small brown fox" ]
```

 

 




