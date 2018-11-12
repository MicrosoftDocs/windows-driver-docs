---
title: dtx (Display Type - Extended Debugger Object Model Information)
description: The dtx command displays extended symbolic type information using the debugger object model. The dtx command is similar to the dt (Display Type) command.
ms.assetid: 758D752E-65A0-4F1D-BB56-06E4ECEC6D48
keywords: ["dtx (Display Type - Extended Debugger Object Model Information) Windows Debugging"]
ms.author: domars
ms.date: 09/17/2017
topic_type:
- apiref
api_name:
- dtx (Display Type - Extended Debugger Object Model Information)
api_type:
- NA
ms.localizationpriority: medium
---

# <span id="debugger.dtx__display_type_-_extended_debugger_object_model_information_"></span>dtx (Display Type - Extended Debugger Object Model Information)


The dtx command displays extended symbolic type information using the debugger object model. The dtx command is similar to the [**dt (Display Type)**](dt--display-type-.md) command.

```dbgcmd
dtx -DisplayOpts [Module!]Name Address
```

## <span id="Parameters"></span><span id="parameters"></span><span id="PARAMETERS"></span>Parameters


<span id="________DisplayOpts_______"></span><span id="________displayopts_______"></span><span id="________DISPLAYOPTS_______"></span> **DisplayOpts**   
Use the following optional flags to change how the output is displayed.

*-a* Displays array elements in a new line with its index.

*-r \[n\]* Recursively dump the subtypes (fields) up to *n* levels.

*-h* Displays command line help for the dtx command.

<span id="Module______________"></span><span id="module______________"></span><span id="MODULE______________"></span>**Module!**   
An optional parameter specifying the module that defines this structure, followed by the exclamation point. If there is a local variable or type with the same name as a global variable or type, you should include *module* name to specify the global variable.

<span id="________Name_______"></span><span id="________name_______"></span><span id="________NAME_______"></span> **Name**   
A type name or a global symbol.

<span id="________Address_______"></span><span id="________address_______"></span><span id="________ADDRESS_______"></span> **Address**   
Memory address containing the type.

### <span id="Environment"></span><span id="environment"></span><span id="ENVIRONMENT"></span>Environment

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<tbody>
<tr class="odd">
<td align="left"><p><strong>Modes</strong></p></td>
<td align="left"><p>user mode, kernel mode</p></td>
</tr>
<tr class="even">
<td align="left"><p><strong>Targets</strong></p></td>
<td align="left"><p>live, crash dump</p></td>
</tr>
<tr class="odd">
<td align="left"><p><strong>Platforms</strong></p></td>
<td align="left"><p>all</p></td>
</tr>
</tbody>
</table>

 

### <span id="Additional_Information"></span><span id="additional_information"></span><span id="ADDITIONAL_INFORMATION"></span>Additional Information

The following examples show how to use the dtx command.

Use the address and the name to display extended symbolic type information.

```dbgcmd
0: kd> dtx nt!_EPROCESS ffffb607560b56c0
(*((nt!_EPROCESS *)0xffffb607560b56c0))                 [Type: _EPROCESS]
    [+0x000] Pcb              [Type: _KPROCESS]
    [+0x2d8] ProcessLock      [Type: _EX_PUSH_LOCK]
    [+0x2e0] RundownProtect   [Type: _EX_RUNDOWN_REF]
    [+0x2e8] UniqueProcessId  : 0x4 [Type: void *]
    [+0x2f0] ActiveProcessLinks [Type: _LIST_ENTRY]
```

Display additional information using the -r recursion option.

```dbgcmd
0: kd> dtx -r2 HdAudio!CAzMixertopoMiniport fffff806`d24992b8
(*((HdAudio!CAzMixertopoMiniport *)0xfffff806d24992b8))                 [Type: CAzMixertopoMiniport]
    [+0x018] m_lRefCount      : -766760880 [Type: long]
    [+0x020] m_pUnknownOuter  : 0xfffff806d24dbc40 [Type: IUnknown *]
    [+0x028] m_FilterDesc     [Type: PCFILTER_DESCRIPTOR]
        [+0x000] Version          : 0xd24c2890 [Type: unsigned long]
        [+0x008] AutomationTable  : 0xfffff806d24c2780 [Type: PCAUTOMATION_TABLE *]
            [+0x000] PropertyItemSize : 0x245c8948 [Type: unsigned long]
            [+0x004] PropertyCount    : 0x6c894808 [Type: unsigned long]
            [+0x008] Properties       : 0x5718247489481024 [Type: PCPROPERTY_ITEM *]
            [+0x010] MethodItemSize   : 0x55415441 [Type: unsigned long]
            [+0x014] MethodCount      : 0x57415641 [Type: unsigned long]
            [+0x018] Methods          : 0x4ce4334540ec8348 [Type: PCMETHOD_ITEM *]
            [+0x020] EventItemSize    : 0x8b41f18b [Type: unsigned long]
            [+0x024] EventCount       : 0xd8b48f4 [Type: unsigned long]
            [+0x028] Events           : 0x7d2d8d4cfffdf854 [Type: PCEVENT_ITEM *]
            [+0x030] Reserved         : 0x66fffd79 [Type: unsigned long]
        [+0x010] PinSize          : 0xd24aa9b0 [Type: unsigned long]
        [+0x014] PinCount         : 0xfffff806 [Type: unsigned long]
        [+0x018] Pins             : 0xfffff806d24aa740 [Type: PCPIN_DESCRIPTOR *]
            [+0x000] MaxGlobalInstanceCount : 0x57555340 [Type: unsigned long]
            [+0x004] MaxFilterInstanceCount : 0x83485741 [Type: unsigned long]
            [+0x008] MinFilterInstanceCount : 0x8b4848ec [Type: unsigned long]
            [+0x010] AutomationTable  : 0xa5158b48ed33c000 [Type: PCAUTOMATION_TABLE *]
            [+0x018] KsPinDescriptor  [Type: KSPIN_DESCRIPTOR]
```

Tip: Use the [**x (Examine Symbols)**](x--examine-symbols-.md) command to display the address of an item of interest.

```dbgcmd
0: kd> x /d HdAudio!CazMixertopoMiniport*
...
fffff806`d24992b8 HdAudio!CAzMixertopoMiniport::`vftable' = <no type information>
...
```

## <span id="see_also"></span>See also


[**dt (Display Type)**](dt--display-type-.md)

 

 






