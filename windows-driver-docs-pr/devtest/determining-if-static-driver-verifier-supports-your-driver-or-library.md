---
title: Determining if Static Driver Verifier supports your driver or library
description: Static Driver Verifier (SDV) can support WDM, KMDF, NDIS, and Storport drivers and libraries. To determine if your driver or library is supported and configured correctly, read over requirements described in this section.
ms.assetid: 29E93E9E-7F87-4706-97AD-DB9A32EDD388
---

# Determining if Static Driver Verifier supports your driver or library


Static Driver Verifier (SDV) can support WDM, KMDF, NDIS, and Storport drivers and libraries. To determine if your driver or library is supported and configured correctly, read over requirements described in this section.

## <span id="driver.library.reqs"></span><span id="DRIVER.LIBRARY.REQS"></span>Driver or library requirements


You can run the SDV analysis tool if your driver or library meets one of following conditions:

-   You have a WDM driver or library, and the driver or library does not link to a class framework (that is, a Microsoft-provided library). For more information, see [Class framework (libraries)](#class-framework-libraries).
-   You have a driver or library that links to WdfLdr.lib or WdfDriverEntry.lib.
-   You have a driver or library that links to NDIS.lib.
-   You have a driver or library that links to Storport.lib.

Static Driver Verifier supports a driver or library that passes those conditions even if the driver or library links to multiple [utility libraries](#known-utility-libraries).

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

## <span id="Visual_Studio_project_requirements"></span><span id="visual_studio_project_requirements"></span><span id="VISUAL_STUDIO_PROJECT_REQUIREMENTS"></span>Visual Studio project requirements


To use Static Driver Verifier, the Visual Studio project must have the following settings:

-   UseDebugLibraries = false
-   Platform = Win32 (x86) or x64

## <span id="class.framework.libraries"></span><span id="CLASS.FRAMEWORK.LIBRARIES"></span>Class framework (libraries)


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

 

## <span id="known.utility.libraries"></span><span id="KNOWN.UTILITY.LIBRARIES"></span>Known utility libraries


Static Driver Verifier supports a driver or library that has links to multiple utility libraries if the driver or library conforms to the [Driver or Library requirements](#driver-library-reqs).

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

 

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[devtest\devtest]:%20Determining%20if%20Static%20Driver%20Verifier%20supports%20your%20driver%20or%20library%20%20RELEASE:%20%2811/17/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




