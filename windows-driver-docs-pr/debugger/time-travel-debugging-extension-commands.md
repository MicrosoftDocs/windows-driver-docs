---
title: !ttdext (time travel)
description: This section describes how to use the time travel debugger extensions.
ms.author: windowsdriverdev
ms.date: 09/20/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

> [!NOTE]
> The information in this topic is preliminary. Updated information will be provided in a later release of the documentation. 
>


# ![Small logo on windbg preview](images/windbgx-preview-logo.png) Time travel debugging extensions

This section describes how to  section describes how to use the how to use the time travel debugger extensions.


## !ttdext navigation commands

Use the !ttdext.tt command to navigate forward or backwards in time, by traveling to a given position in the trace. 

!ttdext.tt {position}

Provide a time position in any of the following formats to travel to that point in time.
           
- If {position} is a decimal number between 0 and 100, it travels to approximately that percent into the trace. For example:
    - !ttdext.tt 0                   - Time travel to the beginning of the trace
    - !ttdext.tt 50                  - Time travel to halfway through the trace
    - !ttdext.tt 100                 - Time travel to the end of the trace
 

- If {position} is #:#, where # are a hexadecimal numbers, it travels to that position. If the number after : is omitted, it defaults to zero.
    - !ttdext.tt 1A0:                - Time travel to position 1A0:0
    - !ttdext.tt 1A0:0               - Time travel to position 1A0:0
    - !ttdext.tt 1A0:12F             - Time travel to position 1A0:12F




## !ttdext Extension utility commands

Use the following !ttdext extension commands to work with TTD traces.


### !ttdext.index

Use !ttdext.*index* to run an indexing pass over the current trace. 

```
0:000> !index
Indexed 10/14 keyframes
Indexed 14/14 keyframes
Successfully created the index in 535ms.

```

If the current trace is already indexed, the !ttdext.index command does nothing.

```
0:000> !ttdext.index
Successfully created the index in 0ms.
```

### !ttdext.index -status

Use !tt.index -status to report the status of the trace index.

```
0:000> !tt.index -status
Index file loaded.
```

??? TBD Table


| Command | Description |
|---------|---------------------------------------------------------------------------|

!search   | Searches trace similar to ba but can be used for registers see TTT-Search  


This section describes the Human Interface Device (HID) debugger extension commands.

The HID debugger extension commands are implemented in Hidkd.dll. To load the HID commands, enter **.load hidkd.dll** in the debugger.

## <span id="Getting_started_with_the_HID_extensions_"></span><span id="getting_started_with_the_hid_extensions_"></span><span id="GETTING_STARTED_WITH_THE_HID_EXTENSIONS_"></span>Getting started with the HID extensions


To start debugging a HID issue, enter the [**!hidtree**](-hidkd-hidtree.md) command. The **!hidtree** command displays a list of commands and addresses that you can use to investigate device objects, preparsed HID data, and HID report descriptors.

## <span id="in_this_section"></span>In this section


<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<thead>
<tr class="header">
<th align="left">Topic</th>
<th align="left">Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td align="left"><p>[<strong>!hidkd.help</strong>](-hidkd-help.md)</p></td>
<td align="left"><p>The [<strong>!hidkd.help</strong>](-hidkd-help.md) command displays help for the HID debugger extension commands.</p></td>
</tr>
<tr class="even">
<td align="left"><p>[<strong>!hidkd.hidfdo</strong>](-hidkd-hidfdo.md)</p></td>
<td align="left"><p>The [<strong>!hidkd.hidfdo</strong>](-hidkd-hidfdo.md) command displays HID information associated with a functional device object (FDO).</p></td>
</tr>
<tr class="odd">
<td align="left"><p>[<strong>!hidkd.hidpdo</strong>](-hidkd-hidpdo.md)</p></td>
<td align="left"><p>The [<strong>!hidkd.hidpdo</strong>](-hidkd-hidpdo.md) command displays HID information associated with a physical device object (PDO).</p></td>
</tr>
<tr class="even">
<td align="left"><p>[<strong>!hidkd.hidtree</strong>](-hidkd-hidtree.md)</p></td>
<td align="left"><p>The [<strong>!hidkd.hidtree</strong>](-hidkd-hidtree.md) command displays a list of all device nodes that have a HID function driver along with their child nodes. The child nodes have a physical device object (PDO) that was created by the parent node's HID function driver.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>[<strong>!hidkd.hidppd</strong>](-hidkd-hidppd.md)</p></td>
<td align="left"><p>The [<strong>!hidkd.hidppd</strong>](-hidkd-hidppd.md) command displays HID preparsed data.</p></td>
</tr>
<tr class="even">
<td align="left"><p>[<strong>!hidkd.hidrd</strong>](-hidkd-hidrd.md)</p></td>
<td align="left"><p>The [<strong>!hidkd.hidrd</strong>](-hidkd-hidrd.md) command displays a HID report descriptor in both raw and parsed format.</p></td>
</tr>
</tbody>
</table>

 
## See Also

[Time Travel Debugging - Overview](time-travel-debugging-overview.md)

---

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[debugger\debugger]:%20HID%20Extensions%20%20RELEASE:%20%285/15/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")





