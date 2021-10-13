---
title: XML Schema Linebreak Translations
description: XML Schema Linebreak Translations
keywords:
- linebreak sequence WDK GDL
- GDL WDK , schemas
- schemas WDK GDL
- snapshots WDK GDL , linebreaks
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# XML Schema Linebreak Translations


The XML snapshot represents linebreaks with the following two character sequence: &lt;0d&gt;&lt;0a&gt; (CR LF). However, within &lt;CDATA&gt; sections, quoted string values, and native XML data type values, the raw character sequence that is found in the GDL source file is used exactly. This usage prevents any loss of information that might be contained in the choice of linebreak sequence that the author of the GDL data uses.

 

 




