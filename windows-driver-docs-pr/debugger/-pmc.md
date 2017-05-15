---
title: pmc
description: The pmc extension displays the Performance Monitor Counter (PMC) register at the specified address.
ms.assetid: ff9a03af-f0e9-4aef-b583-c3092eb5f89c
keywords: ["Performance Monitor Counter (PMC)", "pmc Windows Debugging"]
topic_type:
- apiref
api_name:
- pmc
api_type:
- NA
---

# !pmc


The **!pmc** extension displays the Performance Monitor Counter (PMC) register at the specified address.

This extension is supported only on an Itanium-based target computer.

``` syntax
!pmc [- Option] Expression [DisplayLevel]
```

**Important**  This command has been deprecated in the Windows Debugger Version 10.0.14257 and later, and is no longer available.

 

## <span id="Parameters"></span><span id="parameters"></span><span id="PARAMETERS"></span>Parameters


<span id="_______Option______"></span><span id="_______option______"></span><span id="_______OPTION______"></span> *Option*   
Can be any one of the following values:

<span id="gen"></span><span id="GEN"></span>**gen**  
Displays the register as a generic PMC register.

<span id="btb"></span><span id="BTB"></span>**btb**  
Displays the register as a branch trace buffer (BTB) PMC register.

<span id="_______Expression______"></span><span id="_______expression______"></span><span id="_______EXPRESSION______"></span> *Expression*   
Specifies the hexadecimal address of a PMC. The expressions **@kpfcgen** and **@kpfcbtb** can be used as values for this parameter.

If *Expression* is **@kpfcgen**, the debugger displays the current processor PMC register as a generic PMC register. You can also display the current processor PMC register as a generic PMC register by setting *Option* to **gen** and using **@kpfc4**, **@kpfc5**, **@kpfc6**, or **@kpfc7** for the *Expression* value.

If *Expression* is **@kpfcbtb**, the debugger displays the current processor PMC register as a BTB PMC register. You can also display the current processor PMC register as a BTB PMC register by setting *Option* to **btb** and using @kpfc12 for the *Expression* value.

<span id="_______DisplayLevel______"></span><span id="_______displaylevel______"></span><span id="_______DISPLAYLEVEL______"></span> *DisplayLevel*   
Can be any one of the following values:

<span id="0"></span>**0**  
Displays only the values of each PMC register field. This is the default.

<span id="1"></span>**1**  
Displays detailed information about the PMC register fields that are not reserved or ignored.

<span id="2"></span>**2**  
Displays detailed information about all PMC register fields, including those that are ignored or reserved.

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

 

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[debugger\debugger]:%20!pmc%20%20RELEASE:%20%285/15/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




