---
title: rm (Register Mask)
description: The rm command modifies or displays the register display mask. This mask controls how registers are displayed by the r (Registers) command.
ms.assetid: b3203bf3-b614-490b-8cbd-6abb291a801a
keywords: ["rm (Register Mask) Windows Debugging"]
ms.author: domars
ms.date: 07/12/2018
topic_type:
- apiref
api_name:
- rm (Register Mask)
api_type:
- NA
ms.localizationpriority: medium
---

# rm (Register Mask)


The **rm** command modifies or displays the register display mask. This mask controls how registers are displayed by the [**r (Registers)**](r--registers-.md) command.

```dbgcmd
rm 
rm ? 
rm Mask 
```

## <span id="ddk_cmd_register_mask_dbg"></span><span id="DDK_CMD_REGISTER_MASK_DBG"></span>Parameters


<span id="______________"></span> **?**   
Displays a list of possible *Mask* bits.

<span id="_______Mask______"></span><span id="_______mask______"></span><span id="_______MASK______"></span> *Mask*   
Specifies the mask to use when the debugger displays the registers. *Mask* is a sum of bits that indicate something about the register display. The meaning of the bits depends on the processor and the mode. For more information; see the tables in the following Remarks section.

### <span id="Environment"></span><span id="environment"></span><span id="ENVIRONMENT"></span>Environment

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<tbody>
<tr class="odd">
<td align="left"><p><strong>Modes</strong></p></td>
<td align="left"><p>User mode, kernel mode</p></td>
</tr>
<tr class="even">
<td align="left"><p><strong>Targets</strong></p></td>
<td align="left"><p>Live, crash dump</p></td>
</tr>
<tr class="odd">
<td align="left"><p><strong>Platforms</strong></p></td>
<td align="left"><p>All</p></td>
</tr>
</tbody>
</table>



Remarks
-------

The "m" in the command name must be a lowercase letter.

If you use **rm** with no parameters, the current value is displayed, along with an explanation about its bits.

To display the basic integer registers, you must set bit 0 (0x1) or bit 1 (0x2). By default, 0x1 is set for 32-bit targets and 0x2 is set for 64-bit targets. You cannot set these two bits at the same time--if you try to set both bits, 0x2 overrides 0x1.

You can override the default mask by using the [**r (Registers)**](r--registers-.md) command together with the **M** option.

The following *Mask* bits are supported for an x86-based processor or an x64-based processor.

<table>
<colgroup>
<col width="33%" />
<col width="33%" />
<col width="33%" />
</colgroup>
<thead>
<tr class="header">
<th align="left">Bit</th>
<th align="left">Value</th>
<th align="left">Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td align="left"><p></p>
0
1</td>
<td align="left"><p></p>
0x1
0x2</td>
<td align="left"><p>Displays the basic integer registers. (Setting one or both of these bits has the same effect.)</p></td>
</tr>
<tr class="even">
<td align="left"><p>2</p></td>
<td align="left"><p>0x4</p></td>
<td align="left"><p>Displays the floating-point registers.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>3</p></td>
<td align="left"><p>0x8</p></td>
<td align="left"><p>Displays the segment registers.</p></td>
</tr>
<tr class="even">
<td align="left"><p>4</p></td>
<td align="left"><p>0x10</p></td>
<td align="left"><p>Displays the MMX registers.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>5</p></td>
<td align="left"><p>0x20</p></td>
<td align="left"><p>Displays the debug registers. In kernel mode, setting this bit also displays the CR4 register.</p></td>
</tr>
<tr class="even">
<td align="left"><p>6</p></td>
<td align="left"><p>0x40</p></td>
<td align="left"><p>Displays the SSE XMM registers.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>7</p></td>
<td align="left"><p>0x80</p></td>
<td align="left"><p>(Kernel mode only) Displays the control registers, for example CR0, CR2, CR3 and CR8.</p></td>
</tr>
<tr class="even">
<td align="left"><p>8</p></td>
<td align="left"><p>0x100</p></td>
<td align="left"><p>(Kernel mode only) Displays the descriptor and task state registers.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>9</p></td>
<td align="left"><p>0x200</p></td>
<td align="left"><p>Displays the AVX YMM registers in floating point.</p></td>
</tr>
<tr class="even">
<td align="left"><p>10</p></td>
<td align="left"><p>0x400</p></td>
<td align="left"><p>Displays the AVX YMM registers in decimal integers.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>11</p></td>
<td align="left"><p>0x800</p></td>
<td align="left"><p>Displays the AVX XMM registers in decimal integers.</p></td>
</tr>
<tr class="even">
<td align="left"><p></p>12</td>
<td align="left"><p></p>0x1000</td>
<td align="left"><p>Displays the AVX-512 zmm0-zmm31 registers in floating point format.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>13</p></td>
<td align="left"><p>0x2000</p></td>
<td align="left"><p>Displays the AVX-512 zm00-zmm31 registers in integer format.</p></td>
</tr>
<tr class="even">
<td align="left"><p>14</p></td>
<td align="left"><p>0x4000</p></td>
<td align="left"><p>Displays the AVX-512 k0-k7 registers.</p></td>
</tr>
</tbody>
</table>


## Examples

Enable the integer state and segment registers.

```dbgcmd
0: kd> rm 0x00a
0: kd> rm
Register output mask is a:
       2 - Integer state (64-bit)
       8 - Segment registers
```


Enable 0x1000 (Displays the AVX-512 zmm0-zmm31 registers in floating point format).

```dbgcmd
0: kd> rm 0x100a
0: kd> rm
Register output mask is 100a:
       2 - Integer state (64-bit)
       8 - Segment registers
    1000 - AVX-512 ZMM registers
```


Enable mask 0x2000 (Displays the  AVX-512 zmm00-zmm31 registers in integer format).

```dbgcmd
0: kd> rm 0x200a
0: kd> rm
Register output mask is 200a:
       2 - Integer state (64-bit)
       8 - Segment registers
    2000 - AVX-512 ZMM Integer registers
```


Enable all AVX-512 register masks:

```dbgcmd
0: kd> rm 0x700a
0: kd> rm
Register output mask is 700a:
       2 - Integer state (64-bit)
       8 - Segment registers
    1000 - AVX-512 ZMM registers
    2000 - AVX-512 ZMM Integer registers
    4000 - AVX-512 Opmask registers
```

If you try and set a register mask on hardware that does not support it, the invalid bits of the register mask will be ignored.

```dbgcmd
kd> rm 0x100a
Ignored invalid bits 1000
kd> rm
Register output mask is a:
      2 - Integer state (64-bit)
       8 - Segment registers
```





