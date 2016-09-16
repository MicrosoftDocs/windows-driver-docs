---
title: GDL Exercise Notes
author: windows-driver-content
description: GDL Exercise Notes
MS-HAID:
- 'gplfiles\_4e2d8368-c20b-4077-a948-941710404377.xml'
- 'print.gdl\_exercise\_notes'
MSHAttr:
- 'PreferredSiteName:MSDN'
- 'PreferredLib:/library/windows/hardware'
ms.assetid: 39013410-ad8e-4b1a-9db7-2ec541f08989
keywords: ["GDL WDK , examples", "examples WDK GDL", "tutorials WDK GDL", "GDL WDK , tutorials", "GDL WDK , index tree", "parser WDK GDL , index tree"]
---

# GDL Exercise Notes


The following code example shows the index tree that the parser generates for all of the GDL exercises.

```
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

```
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

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bprint\print%5D:%20GDL%20Exercise%20Notes%20%20RELEASE:%20%289/1/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


