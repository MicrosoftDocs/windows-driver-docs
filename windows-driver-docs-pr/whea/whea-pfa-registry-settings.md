---
title: WHEA Policy Settings
author: windows-driver-content
description: WHEA Policy Settings
ms.assetid: 65ef70b7-a517-4428-9e6d-09c6da84e798
keywords:
- predictive failure analysis (PFA) WDK WHEA , registry settings
- registry settings WDK WHEA
- registry settings WDK WHEA , predictive failure analysis (PFA)
- policy settings WDK WHEA
ms.author: windowsdriverdev
ms.date: 04/20/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# WHEA Policy Settings


Predictive Failure Analysis (PFA), as performed by the Windows Hardware Error Architecture (WHEA), is configured by using registry settings. WHEA reads these registry settings when a computer system starts. Any change that you make to these settings requires you to restart the system in order for them to take effect.

Starting with Windows 8, WHEA policies can be managed either though [**WHEAPolicyManagementMethods**](https://msdn.microsoft.com/library/windows/hardware/hh451252) or through the WHEA Powershell module. If the policy is updated through either of these modes, the policy values take effect immediately.

**Note**   The registry settings described in this topic are intended for use by WHEA only. If a [platform-specific hardware error driver (PSHED) plug-in](platform-specific-hardware-error-driver-plug-ins2.md) performs PFA and uses the registry to store its configuration settings, it must use registry values that are different from those that are described in this topic.

 

The WHEA PFA configuration settings are located in the following registry key:

```
HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Control\WHEA\Policy
```

**Note**  WHEA assumes the default setting for a PFA registry value if that value is not present under **HKEY\_LOCAL\_MACHINE\\SYSTEM\\CurrentControlSet\\Control\\WHEA\\Policy**.

 

The following table describes the various registry values that are used for PFA configuration. The registry values in the following table are REG\_DWORD values.

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<thead>
<tr class="header">
<th>Registry value name</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><p></p>
<p><strong>DisableOffline</strong></p></td>
<td><p>A Boolean value that specifies whether WHEA can take hardware components offline by using PFA. WHEA takes a hardware component, such as an ECC memory page, offline whenever PFA (performed by WHEA or a PSHED plug-in) determines the module has exceeded an error threshold.</p>
<div class="alert">
<strong>Note</strong>  The <strong>DisableOffline</strong> value applies to hardware components that are predicted to fail due to PFA performed either by WHEA or a PSHED plug-in.
</div>
<div>
 
</div>
<p>A value of 0 enables hardware offline support. Any other value disables hardware offline support.</p>
<p>The default value for this setting is 0.</p></td>
</tr>
<tr class="even">
<td><p></p>
<p><strong>MemPersistOffline</strong></p></td>
<td><p>A Boolean value that specifies whether the ECC memory pages that WHEA took offline persist in the Boot Configuration Data (BCD) store. If persisted within the BCD store, the ECC memory pages will be taken offline immediately after a system has been restarted.</p>
<div class="alert">
<strong>Note</strong>  The <strong>MemPersistOffline</strong> value applies to ECC memory pages taken offline due to PFA performed either by WHEA or a PSHED plug-in.
</div>
<div>
 
</div>
<p>A value of 1 enables BCD persistence. A value of 0 disables BCD persistence.</p>
<p>The default value for this setting is 1 for Windows Server platforms and 0 for Windows client platforms.</p></td>
</tr>
<tr class="odd">
<td><p></p>
<p><strong>MemPfaDisable</strong></p></td>
<td><p>A Boolean value that specifies whether WHEA's PFA for ECC memory pages is disabled.</p>
<p>A value of 0 enables PFA for ECC memory pages. Any other value disables PFA for ECC memory pages.</p>
<p>The default value for this setting is 0.</p></td>
</tr>
<tr class="even">
<td><p></p>
<p><strong>MemPfaPageCount</strong></p></td>
<td><p>A value that specifies the maximum number of ECC memory pages that WHEA monitors for PFA.</p>
<p>This value can be between 1 and 65536. The default value is 64.</p>
<div class="alert">
<strong>Note</strong>  If this value is set to a number that is outside the allowable range, the default value is used.
</div>
<div>
 
</div></td>
</tr>
<tr class="odd">
<td><p></p>
<p><strong>MemPfaThreshold</strong></p></td>
<td><p>A value that specifies the maximum number of errors allowed on an ECC memory page that WHEA is monitoring.</p>
<p>When the number of errors exceeds this threshold, WHEA stops monitoring the memory page and attempts to take the memory page offline.</p>
<p>This value can be between 1 and 65536. The default value is 16.</p>
<div class="alert">
<strong>Note</strong>  If this value is set to a number that is outside the allowable range, the default value is used.
</div>
<div>
 
</div></td>
</tr>
<tr class="even">
<td><p></p>
<p><strong>MemPfaTimeout</strong></p></td>
<td><p>A value, in units of seconds, that specifies how long an ECC memory page is monitored by WHEA for PFA.</p>
<p>WHEA starts to monitor an ECC memory page when the first error is detected for that memory page.</p>
<p>WHEA stops monitoring an ECC memory page when one of the following has occurred:</p>
<ul>
<li><p>The monitoring interval has exceeded the <strong>MemPfaTimeout</strong> value.</p></li>
<li><p>The number of detected errors has exceeded the <strong>MemPfaThreshold</strong> value.</p></li>
</ul>
<p>This value can be between 0 and 604800 (7 days). A value of zero specifies that the monitored memory pages will never time out. The default value is 86400 (24 hours).</p>
<div class="alert">
<strong>Note</strong>  If this value is set to a number that is outside the allowable range, the default value is used.
</div>
<div>
 
</div></td>
</tr>
</tbody>
</table>

 

The following two legacy registry values are supported for application compatibility reasons:

<a href="" id="singlebiteccerrorthreshold"></a>**SingleBitEccErrorThreshold**  
This value corresponds to the **MemPfaThreshold** registry value.

<a href="" id="maxcorrectedmceoutstanding"></a>**MaxCorrectedMCEOutstanding**  
This value corresponds to the **MemPfaPageCount** registry value.

**Note**  Whenever possible, you should use the registry values that were described earlier in this topic instead of these legacy registry values.

 

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bwhea\whea%5D:%20WHEA%20Policy%20Settings%20%20RELEASE:%20%289/14/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


