---
title: isr
description: The isr extension displays the Itanium Interruption Status Register (ISR) at the specified address.
ms.assetid: 35cf1749-2417-4fd9-9de2-0884ee795ab3
keywords: ["ISR (Interruption Status Register)", "Interruption Status Register (ISR)", "isr Windows Debugging"]
ms.author: domars
ms.date: 05/23/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
topic_type:
- apiref
api_name:
- isr
api_type:
- NA
---

# !isr


The !isr extension displays the Itanium Interruption Status Register (ISR) at the specified address.

```
!isr Expression [DisplayLevel]
```

**Important**  This command has been deprecated in the Windows Debugger Version 10.0.14257 and later, and is no longer available.

 

## <span id="Parameters"></span><span id="parameters"></span><span id="PARAMETERS"></span>Parameters


<span id="_______Expression______"></span><span id="_______expression______"></span><span id="_______EXPRESSION______"></span> *Expression*   
Specifies the hexadecimal address of the ISR register to display. The expression **@isr** can also be used for this parameter. In that case, information about the current processor ISR register is displayed.

<span id="_______DisplayLevel______"></span><span id="_______displaylevel______"></span><span id="_______DISPLAYLEVEL______"></span> *DisplayLevel*   
Can be any one of the following options:

<span id="0"></span>**0**  
Displays only the values of each ISR field. This is the default.

<span id="1"></span>**1**  
Displays detailed information about ISR fields that are not reserved or ignored.

<span id="2"></span>**2**  
Displays details about all ISR fields, including those that are ignored or reserved.

### <span id="DLL"></span><span id="dll"></span>DLL

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<tbody>
<tr class="odd">
<td align="left"><p><strong>Windows 2000</strong></p></td>
<td align="left"><p>Unavailable</p></td>
</tr>
<tr class="even">
<td align="left"><p><strong>Windows XP and later</strong></p></td>
<td align="left"><p>Kdexts.dll</p></td>
</tr>
</tbody>
</table>

 

This extension command can only be used with an Itanium target computer.

Remarks
-------

Here are a couple of examples of output from this extension:

```
kd> !isr @isr
isr:ed ei so ni ir rs sp na r w x vector code
  0  0  0  0  0  0  0  0 0 0 0      0   0

kd> !isr @isr 2

 cod : 0 : interruption Code
 vec : 0 : IA32 exception vector number
  rv : 0 : reserved0
   x : 0 : eXecute exception
   w : 0 : Write exception
   r : 0 : Read exception
  na : 0 : Non-Access exception
  sp : 0 : Speculative load exception
  rs : 0 : Register Stack
  ir : 0 : Invalid Register frame
  ni : 0 : Nested Interruption
  so : 0 : IA32 Supervisor Override
  ei : 0 : Exception IA64 Instruction
  ed : 0 : Exception Deferral
  rv : 0 : reserved1
```

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[debugger\debugger]:%20!isr%20%20RELEASE:%20%285/15/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




