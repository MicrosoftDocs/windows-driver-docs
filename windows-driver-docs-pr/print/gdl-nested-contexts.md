---
title: GDL Nested Contexts
author: windows-driver-content
description: GDL Nested Contexts
ms.assetid: c679937a-fa36-487a-84f2-f61a7ef0198e
keywords:
- GDL WDK , contexts
- contexts WDK GDL , nested contexts
- nested contexts WDL GDL
- GDL WDK , values
- values WDK GDL , nested contexts
ms.author: windows-driver-content
ms.date: 04/20/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# GDL Nested Contexts


A *nested context* is introduced with the *begin nesting character* (which is an opening parenthesis or an opening square bracket). The nested context ends when the matching *end nesting character* (which is a closing parenthesis or closing square bracket) is encountered.

Nesting contexts can be nested within each other. The end nesting characters can be used only to end the current nesting context. If end nesting characters appear anywhere else, it is a syntax error.

Within a nested context, the [construct delimiter characters](gdl-construct-delimiters.md) lose their meaning as construct delimiters and are also treated as nested context delimiters. Within a nested context, a linebreak sequence is treated as non-literal whitespace.

The nested context can appear outside of any context or within another nested context but not within any other context. Any context, including other nested contexts, can appear within a nested context, except for the HexSubString context.

The following code example shows a GDL nested context.

```
*good_nests: ( { } [ ( ) ] )
```

The following code examples shows GDL nested contexts that contain errors.

```
*bad_nests: (  ] *%  end nesting delimiter can only be used within its nesting context.
*bad_nests: (  ]  )
*bad_nests:   ] [   *%  end nesting delimiter can only be used within its nesting context.
*bad_nests: (  [  )   ]   *%  end nesting delimiter can only be used within its nesting*% context.  In this case the &#39;)&#39; char cannot be used within the context begun 
*%by &#39;[&#39; .
*bad_nests:  {  [ ]  }  *% attempt to use construct delimiter to define a nesting context 
*%  outside of a nesting context.
```

The entire contents of a nested context is treated as part of the [value](gdl-values.md). For example, the following GDL code represents one entry with a keyword of "\*KeywordA". The remainder of the fragment is the value of \*KeywordA, because what appears to be separate entries for \*KeywordB and \*KeywordC are contained within a nested context. In fact, the numbers "12, 38, 709" are themselves in a nested context that is defined by parentheses delimiters that are nested within the outer context that is defined by the square bracket delimiters.

```
*KeywordA: [
*KeywordB:  List(12, 38, 709)
*KeywordC:  "the small brown fox" ]
```

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bprint\print%5D:%20GDL%20Nested%20Contexts%20%20RELEASE:%20%289/1/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


