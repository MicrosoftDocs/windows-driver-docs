---
title: "!amli find (WinDbg)"
description: "The !amli find extension finds an ACPI namespace object."
keywords: ["!amli find Windows Debugging"]
ms.date: 09/17/2018
topic_type:
- apiref
ms.topic: reference
api_name:
- amli find
api_type:
- NA
---

# !amli find


The **!amli find** extension finds an ACPI namespace object.

Syntax

```dbgcmd
    !amli find Name
```

## <span id="ddk__amli_find_dbg"></span><span id="DDK__AMLI_FIND_DBG"></span>Parameters


<span id="_______Name______"></span><span id="_______name______"></span><span id="_______NAME______"></span> *Name*   
Specifies the name of the namespace object (without the path).

## DLL

Kdexts.dll

### Additional Information

For information about related commands and their uses, see [The AMLI Debugger](../debugger/the-amli-debugger.md).

## Remarks

The **!amli find** command takes the name of the object and returns the full path and name. The *Name* parameter must be the final segment of the full path and name.

Here are some examples. The following command will find all declarations of the object \_SRS:

```console
kd> !amli find _srs
\_SB.LNKA._SRS
\_SB.LNKB._SRS
\_SB.LNKC._SRS
\_SB.LNKD._SRS
```

This is not simply a text search. The command **!amli find srs** does not display any hits, because the final segment of each of these declarations is "\_SRS", not "SRS". The command **!amli find LNK** similarly does not return hits. The command **!amli find LNKB** would display the single node that terminates in "LNKB", not the four children of this node shown in the previous display:

```console
kd> !amli find lnkb
\_SB.LNKB.
```

If you need to see the children of a node, use the [**!amli dns**](-amli-dns.md) command with the **/s** parameter.

Here is another example, issued from the AMLI Debugger prompt. This shows all declarations of the object \_BST in the namespace:

```console
AMLI(? for help)-> find _bst
\_SB.PCI0.ISA.BAT1._BST
\_SB.PCI0.ISA.BAT2._BST
```

 

 





