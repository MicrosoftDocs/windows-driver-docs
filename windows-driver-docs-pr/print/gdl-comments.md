---
title: GDL Comments
author: windows-driver-content
description: GDL Comments
ms.assetid: d7103c5b-87dd-46e9-972a-188758ee3447
keywords:
- constructs WDK GDL , comments
- comments WDK GDL
- contexts WDK GDL , comments
- GDL WDK , comments
ms.author: windowsdriverdev
ms.date: 04/20/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
ms.localizationpriority: medium
---

# GDL Comments


A *comment* can appear anywhere that [non-literal whitespace](gdl-whitespace-characters.md) can appear. A comment begins with an asterisk and percent sign (\*%) and ends when a linebreak sequence or continuation linebreak is encountered.

The entire comment is treated as non-literal whitespace. The terminating linebreak sequence is not part of the comment. Comments can appear within a nested context, but no contexts are recognized within a comment.

 

 




