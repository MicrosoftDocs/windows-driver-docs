---
title: GDL Exercise Notes
description: GDL Exercise Notes
ms.assetid: 39013410-ad8e-4b1a-9db7-2ec541f08989
keywords:
- GDL WDK , examples
- examples WDK GDL
- tutorials WDK GDL
- GDL WDK , tutorials
- GDL WDK , index tree
- parser WDK GDL , index tree
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# GDL Exercise Notes


The following code example shows the index tree that the parser generates for all of the GDL exercises.

```cpp
      <:ROOT2>
    *PFeature : InputTray    <:INPUTTRAY_FEATURE>
        *POption : Lower    <:INPUTTRAY_OPTION2>
            *Capacity    <:TRAY_CAPACITY>
            *Command    <:ACOMMAND>
            *Name    <:INPUTTRAY_OPT_NAME>
        *POption : Upper    <:INPUTTRAY_OPTION2>
            *Capacity    <:TRAY_CAPACITY>
            *Command    <:ACOMMAND>
            *Name    <:INPUTTRAY_OPT_NAME>
        *DefaultOption    <:DEFAULT_OPT>
        *Name    <:NAME>
    *PFeature : PaperSize    <:PAPERSIZE_FEATURE>
        *POption : Custom    <:CUST_PAPERSIZE_OPTION>
            *MinSize    <:MIN_SIZE>
            *MaxSize    <:MAX_SIZE>
            *Command    <:ACOMMAND>
            *Name    <:PAPER_SIZE_OPT_NAME>
        *POption : OEMName_Special_size    <:OEM_PAPERSIZE_OPTION>
            *OEM_Info    <:OEM_INFO>
            *PaperSize    <:PAPERDIMENSIONS>
            *Command    <:ACOMMAND>
            *Name    <:PAPER_SIZE_OPT_NAME>
        *POption : A4    <:PREDEFINED_PAPERSIZE_OPTION>
            *PaperSize    <:PAPERDIMENSIONS>
            *Command    <:ACOMMAND>
            *Name    <:PAPER_SIZE_OPT_NAME>
        *POption : Legal    <:PREDEFINED_PAPERSIZE_OPTION>
            *PaperSize    <:PAPERDIMENSIONS>
            *Command    <:ACOMMAND>
            *Name    <:PAPER_SIZE_OPT_NAME>
        *POption : Letter    <:PREDEFINED_PAPERSIZE_OPTION>
            *PaperSize    <:PAPERDIMENSIONS>
            *Command    <:ACOMMAND>
            *Name    <:PAPER_SIZE_OPT_NAME>
        *DefaultOption    <:DEFAULT_OPT>
        *Name    <:NAME>
    *PFeature : random    <:PFEATURE >
        *POption : First    <:GENERIC_OPTION>
            *Command    <:ACOMMAND>
            *Name    <:NAME>
        *DefaultOption    <:DEFAULT_OPT>
        *Name    <:NAME>
```

The \*Name and \*POption entries map to several templates, each with different semantics. For example, \*Name maps to NAME, INPUTTRAY\_OPT\_NAME, or PAPER\_SIZE\_OPT\_NAME. \*POption maps to GENERIC\_OPTION, PREDEFINED\_PAPERSIZE\_OPTION, CUST\_PAPERSIZE\_OPTION, OEM\_PAPERSIZE\_OPTION, or INPUTTRAY\_OPTION2. If the template structure has been defined correctly, the parser following its templatization rules will find the most appropriate template.

**Note**   These exercises establish some basic templates and subsequently derived variants as the schema became more detailed. This process mimics the way a schema evolves in real-life. Inheritance enabled the exercise schema to be extended without changing any previously defined templates. This feature enables third parties to extend the master schema and also ensures that any third-party schema extension remains compatible with users of the original master schema.

 

The exercise answers that are shown are not unique. For example, you could have derived the templates MIN\_SIZE and MAX\_SIZE from PAPERDIMENSIONS in the following manner.

```cpp
*Template:  MIN_SIZE
{
    *Name: "*MinSize"
    *Inherits: PAPERDIMENSIONS
}
*Template:  MAX_SIZE
{
    *Name: "*MaxSize"
    *Inherits: PAPERDIMENSIONS
}
```

Note that the PAPER\_SIZE\_OPT\_NAME and INPUTTRAY\_OPT\_NAME templates inherit from the template NAME and also redefine the \*Name entry.

The effect of redefining the \*Name entry is to hide these derived templates from the inheritance tree that the base templates establish.

Typically, when a template declares NAME to be a \*Member, this declaration implies that all templates that are derived from NAME are also \*Members. However, derived templates with redefined \*Name entries are excluded from the implied \*Members list of derived templates. Without this exclusion, data entries that would have originally mapped to template NAME (for example, \*Name appearing within a \*Pfeature) would get mapped to INPUTTRAY\_OPT\_NAME (which is incorrect).

If you anticipate the specialization of NAME into PAPER\_SIZE\_OPT\_NAME and INPUTTRAY\_OPT\_NAME during the original design of the schema, a different schema implementation would result simply by removing NAME from the \*Members list of GENERIC\_OPTION. This change would make it unnecessary to redefine \*Name. A further design refinement would have NAME, PAPER\_SIZE\_OPT\_NAME, and INPUTTRAY\_OPT\_NAME inheriting from a common virtual template, because that situation more accurately reflects the relationship between these keywords.

 

 




