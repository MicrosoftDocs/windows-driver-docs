---
title: GDL Source File Preprocessor Directives
description: GDL Source File Preprocessor Directives
ms.assetid: cc0f807f-5c06-4add-bed1-c15c8251dc98
keywords:
- directives WDK GDL , source file preprocessor directives
- source files WDK GDL , preprocessor directives
- preprocessor directives WDK GDL
- parser WDK GDL , directives
- Include directive WDK GDL
- PreCompiled directive WDK GDL
- Define directive WDK GDL
- Undefine directive WDK GDL
- Ifdef directive WDK GDL
- Elseifdef directive WDK GDL
- Else directive WDK GDL
- Endif directive WDK GDL
- SetPPPrefix directive WDK GDL
- UndefinePrefix directive WDK GDL
- EnablePPDirective directive WDK GDL
- DisablePPDirective directive WDK GDL
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# GDL Source File Preprocessor Directives


The GDL parser, like the original GPD parser, supports preprocessor directives. The preprocessor directives are processed before any other parsing. During the preprocessing phase, only the preprocessor directives are recognized and all non-directive entries are treated as black-box data. During the preprocessing phrase, all preprocessor directives are removed from the input stream so the subsequent parsing phase does not need to contend with the preprocessor syntax.

The purpose of the preprocessor directives is to enable you to create a single GDL file that runs on multiple versions of a GDL or GPD parser. If you have parser features that occur only on some parser versions, you can use an **\#Ifdef** statement and replace the feature by equivalent entries.

Preprocessor directives use a specific [GDL preprocessor syntax](gdl-preprocessor-syntax.md) and [GDL preprocessor keywords](gdl-preprocessor-keywords.md).

GDL preprocessor directives are an extension of GPD preprocessor directives. For more information about the differences between GDL and GPD preprocessor directives, see [Differences Between GDL and GPD Preprocessing](differences-between-gdl-and-gpd-preprocessing.md).

GDL preprocessor directives are only one kind of GDL directive. For more information about other types of GDL directives, see [GDL Directives](gdl-directives.md).

The following list is a summary of GDL preprocessor keywords:

-   **\#Include** references another GDL file for inclusion into the current GDL file.

-   **\#Define** and **\#Undefine** manage list of symbols that the preprocessor conditional directives use.

-   **\#PreCompiled** creates a stand-alone data structure that represents the GDL source file that is contained in this file that can be dynamically linked to the GDL data structure that represents another GDL file. You can use this directive to eliminate redundant copies of frequently used files.

-   **\#Ifdef**, **\#Elseifdef**, **\#Else**, and **\#Endif** conditionally disable sections within a GDL source file. These directives can reference symbols that are defined by the preprocessor conditional directives or symbols that are defined by different versions of the GDL parser.

-   **\#SetPPPrefix**, **\#UndefinePrefix**, **\#EnablePPDirective**, and **\#DisablePPDirective** modify the processing of directives.

This section includes:

[GDL Preprocessor Syntax](gdl-preprocessor-syntax.md)

[GDL Preprocessor Keywords](gdl-preprocessor-keywords.md)

[Differences Between GDL and GPD Preprocessing](differences-between-gdl-and-gpd-preprocessing.md)

[GDL Preprocessor Guidelines](gdl-preprocessor-guidelines.md)

 

 




