---
title: GDL Arbitrary Value Contexts
description: GDL Arbitrary Value Contexts
ms.assetid: 6de79b2b-5f0f-4d6c-8a95-d9ef2266c2ef
keywords:
- GDL WDK , contexts
- contexts WDK GDL , arbitrary value contexts
- arbitrary value contexts WDK GDL
- values WDK GDL , contexts
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# GDL Arbitrary Value Contexts


An *arbitrary value context* is used to define values that contain any arbitrary sequence of characters even if they violate the GDL syntax rules.

The arbitrary value context is introduced when the "&lt;BeginValue:*symbol*&gt;" character sequence is encountered and terminates when the "&lt;EndValue:*symbol*&gt;" character sequence is encountered. *symbol* is any valid symbol token that you choose. The same symbol must appear in both the BeginValue and EndValue invocation. No whitespaces can appear in the BeginValue and EndValue tags.

An arbitrary value context can be defined in any value context except within a comment or a quoted string. The arbitrary value context can appear within a nested context. No contexts are recognized within the arbitrary value context, but any sequence of bytes can be defined within.

An arbitrary value context symbol is a token that consists of characters from the set \[A-Z, a-z, 0-9, \_ \]. There is no limit to the length of a symbol.

 

 




