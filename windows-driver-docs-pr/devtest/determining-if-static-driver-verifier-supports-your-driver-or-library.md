---
title: Determining if Static Driver Verifier supports your driver or library
description: Static Driver Verifier (SDV) can support WDM, KMDF, NDIS, and Storport drivers and libraries. To determine if your driver or library is supported and configured correctly, read over requirements described in this section.
ms.assetid: 29E93E9E-7F87-4706-97AD-DB9A32EDD388
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Determining if Static Driver Verifier supports your driver or library


Static Driver Verifier (SDV) fully supports WDM, KMDF, NDIS, and Storport drivers and libraries, and has limited support for other drivers. To determine if your driver or library is supported and configured correctly, read over requirements described in this section.

## Driver or library requirements


You can run the full set of rules in the SDV analysis tool if your driver or library meets one of following conditions:

-   You have a WDM driver or library, and the driver or library does not link to a class framework (that is, a Microsoft-provided library). For more information, see [Class framework libraries](#class-framework-libraries).
-   You have a driver or library that links to WdfLdr.lib or WdfDriverEntry.lib.
-   You have a driver or library that links to NDIS.lib.
-   You have a driver or library that links to Storport.lib.

Static Driver Verifier supports a driver or library that passes those conditions even if the driver or library links to multiple [utility libraries](#utility-libraries).

In addition, to perform the analysis, SDV requires that:

-   The driver has declared at least one entry point [Using Function Role Type Declarations](using-function-role-type-declarations.md).
-   The driver builds and links correctly (in Visual Studio using MSBuild).
-   If the driver or library uses KMDF, the driver or library uses KDMF version 1.7 or later.
-   If the driver or library uses NDIS, it uses NDIS version 6.0, 6.1, 6.20, 6.30, or 6.40. Note that this list is subject to change.
-   The driver does not combine driver models (for example, KMDF with WDM, or KMDF and NDIS).

There are other factors that affect the quality and accuracy of the static analysis results. These factors include:

-   Use of utility libraries that have not been processed by SDV.
-   Size of the driver, particularly if it has more than 100K lines of code.
-   Use of language-specific features, such as virtual functions and pointer arithmetic.

## Visual Studio project requirements


To use Static Driver Verifier, the Visual Studio project must have the following settings:

-   UseDebugLibraries = false
-   Platform = Win32 (x86) or x64

## Class framework libraries


If you have a WDM driver or library and want to run SDV, the driver or library must not link to one of the following class framework libraries.

<table>
<colgroup>
<col width="25%" />
<col width="25%" />
<col width="25%" />
<col width="25%" />
</colgroup>
<tbody>
<tr class="odd">
<td align="left">1394bus.lib</td>
<td align="left">fltMgr.lib</td>
<td align="left">rdbss.lib</td>
<td align="left">usbrpm.lib</td>
</tr>
<tr class="even">
<td align="left">acpi.lib</td>
<td align="left">FsDepends.lib</td>
<td align="left">RNDISMP.lib</td>
<td align="left">videoprt.lib</td>
</tr>
<tr class="odd">
<td align="left">armppm.lib</td>
<td align="left">fwpkclnt.lib</td>
<td align="left">RNDISMP6.lib</td>
<td align="left">vwififlt.lib</td>
</tr>
<tr class="even">
<td align="left">ataport.lib</td>
<td align="left">hidclass.lib</td>
<td align="left">RNDISMPX.lib</td>
<td align="left">watchdog.lib</td>
</tr>
<tr class="odd">
<td align="left">ath_hwpci.lib</td>
<td align="left">hidparse.lib</td>
<td align="left">rpcxdr.lib</td>
<td align="left">win32k.lib</td>
</tr>
<tr class="even">
<td align="left">athhal.lib</td>
<td align="left">hwpolicy.lib</td>
<td align="left">Saha.lib</td>
<td align="left">winhv.lib</td>
</tr>
<tr class="odd">
<td align="left">battc.lib</td>
<td align="left">ipmidrv_hrmcust.lib</td>
<td align="left">scsiport.lib</td>
<td align="left">WMBBCLASS.lib</td>
</tr>
<tr class="even">
<td align="left">BdaSup.lib</td>
<td align="left">irt30.lib</td>
<td align="left">smclib.lib</td>
<td align="left"></td>
</tr>
<tr class="odd">
<td align="left">bdl.lib</td>
<td align="left">irt30.lib</td>
<td align="left">Soft1667FaultInjectionLimpetPool.lib</td>
<td align="left"></td>
</tr>
<tr class="even">
<td align="left">btampm.lib</td>
<td align="left">ks.lib</td>
<td align="left">SoftFCKernel.lib</td>
<td align="left"></td>
</tr>
<tr class="odd">
<td align="left">bthport.lib</td>
<td align="left">ksecdd.lib</td>
<td align="left">SoftFCLimpetPool.lib</td>
<td align="left"></td>
</tr>
<tr class="even">
<td align="left">BTHPRINT.lib</td>
<td align="left">ksmartcpu.lib</td>
<td align="left">SoftSATAKernel.lib</td>
<td align="left"></td>
</tr>
<tr class="odd">
<td align="left">classpnp.lib</td>
<td align="left">mcd.lib</td>
<td align="left">SoftStorageLimpetPool.lib</td>
<td align="left"></td>
</tr>
<tr class="even">
<td align="left">clfs.lib</td>
<td align="left">mpio.lib</td>
<td align="left">srvnet.lib</td>
<td align="left"></td>
</tr>
<tr class="odd">
<td align="left">cng.lib</td>
<td align="left">mrxsmb.lib</td>
<td align="left">storvsp.lib</td>
<td align="left"></td>
</tr>
<tr class="even">
<td align="left">crashdmp.lib</td>
<td align="left">msnfsflt.lib</td>
<td align="left">stream.lib</td>
<td align="left"></td>
</tr>
<tr class="odd">
<td align="left">csr_vfp_avdtp.lib</td>
<td align="left">msrpc.lib</td>
<td align="left">tape.lib</td>
<td align="left"></td>
</tr>
<tr class="even">
<td align="left">diskdump.lib</td>
<td align="left">mup.lib</td>
<td align="left">tbs.lib</td>
<td align="left"></td>
</tr>
<tr class="odd">
<td align="left">drmk.lib</td>
<td align="left">ndistapi.lib</td>
<td align="left">tcpip.lib</td>
<td align="left"></td>
</tr>
<tr class="even">
<td align="left">dumpata.lib</td>
<td align="left">netio.lib</td>
<td align="left">tdi.lib</td>
<td align="left"></td>
</tr>
<tr class="odd">
<td align="left">dumpfve.lib</td>
<td align="left">ntasn1k.lib</td>
<td align="left">termdd.lib</td>
<td align="left"></td>
</tr>
<tr class="even">
<td align="left">dxapi.lib</td>
<td align="left">parallel.lib</td>
<td align="left">USBCAMD.lib</td>
<td align="left"></td>
</tr>
<tr class="odd">
<td align="left">dxg.lib</td>
<td align="left">pciidex.lib</td>
<td align="left">USBCAMD2.lib</td>
<td align="left"></td>
</tr>
<tr class="even">
<td align="left">dxgkrnl.lib</td>
<td align="left">portcls.lib</td>
<td align="left">usbd.lib</td>
<td align="left"></td>
</tr>
<tr class="odd">
<td align="left">dxgmms1.lib</td>
<td align="left">protogon.lib</td>
<td align="left">usbport.lib</td>
<td align="left"></td>
</tr>
</tbody>
</table>

 

## Utility libraries


Static Driver Verifier supports a driver or library that has links to multiple utility libraries if the driver or library conforms to the [Driver or Library requirements](#driver-or-library-requirements).

|                     |
|---------------------|
| BufferOverflowK.lib |
| hal.lib             |
| ntoskrnl.lib        |
| ntstrsafe.lib       |
| rtlver.lib          |
| sehupd.lib          |
| wdm.lib             |
| wmilib.lib          |
| wdmsec.lib          |

 

 

 





