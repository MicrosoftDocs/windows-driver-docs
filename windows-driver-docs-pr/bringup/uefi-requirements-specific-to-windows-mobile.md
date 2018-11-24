---
title: UEFI requirements for Windows 10 Mobile
description: In addition to UEFI requirements that apply to all Windows editions, Windows 10 Mobile devices must meet additional requirements described in this topic.
ms.assetid: 12a03f5b-1717-4daf-90ef-5e530f72b19e
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# UEFI requirements for Windows 10 Mobile


In addition to the UEFI requirements listed in [UEFI requirements that apply to all Windows editions](uefi-requirements-that-apply-to-all-windows-platforms.md), devices that run Windows 10 Mobile must also meet the additional requirements described in this topic.

## Requirements that expand on the general UEFI requirements for all Windows editions


The following table describes the UEFI requirements for Windows 10 Mobile that expand on those requirements described in [UEFI requirements that apply to all Windows editions](uefi-requirements-that-apply-to-all-windows-platforms.md).

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<thead>
<tr class="header">
<th>Requirement</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>GPT</td>
<td>The device must be able to boot from the GUID Partition Table (GPT). Additionally, the device must include both a primary and backup GPT as described in section 5.3 titled “GUID Partition Table Disk Layout” of the UEFI specification.</td>
</tr>
<tr class="even">
<td>Variable services</td>
<td>Variable services must provide at least 64 KB of non-volatile storage for use by Microsoft. Additionally, these variable services must be implemented in a marked location of storage. This requirement is necessary to have sufficient space to store keys and other parameters for secure boot, to allow for flashing the entire storage with new variables, and to allow for the exclusion of these variables when flashing the entire storage. To reduce BOM cost and hardware complexity, Microsoft requires that variable services must not be implemented through the addition of an extra flash part to the device.</td>
</tr>
<tr class="odd">
<td>Simple text input protocol</td>
<td><p>The following physical keys shall map to the following functions:</p>
<ul>
<li>Volume up: Up arrow</li>
<li>Volume up: Down arrow</li>
<li>Camera: Enter</li>
<li>Power button: Suspend</li>
</ul></td>
</tr>
<tr class="even">
<td>Memory services</td>
<td>The GetMemoryMap() function must return the full range of physical memory for the platform, as specified by section 6.2 &quot;Memory Services&quot; of the UEFI specification.</td>
</tr>
<tr class="odd">
<td>EFI block I/O protocol</td>
<td>The EFI block I/O protocol must report a storage devices size based on its native sector size. For example, a 4-KB sector device should not report itself as a 512-byte sector device.</td>
</tr>
</tbody>
</table>



## Requirements specific to Windows 10 Mobile


The following table describes the requirements that are specific to Windows 10 Mobile.

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<thead>
<tr class="header">
<th>Requirement</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>UEFI drivers</td>
<td>UEFI drivers must be embedded in the UEFI firmware.</td>
</tr>
<tr class="even">
<td>USB function protocol</td>
<td>The UEFI firmware must include a driver that adheres to the UEFI USB function protocol. For more information, see <a href="uefi-usb-function-protocol.md" data-raw-source="[UEFI USB function protocol](uefi-usb-function-protocol.md)">UEFI USB function protocol</a>. USB enumeration in UEFI shall only be handled by Microsoft code.</td>
</tr>
<tr class="odd">
<td>Battery charging protocol</td>
<td><p>If the device uses the Microsoft UEFI battery charging application, the UEFI firmware must include a driver that implements the UEFI battery charging protocol. Before the device hands off to the Microsoft UEFI battery charging software, the device must comply with the <em>USB Battery Charging v1.2 Specification</em>. For more information, see <a href="uefi-battery-charging-protocol.md" data-raw-source="[UEFI battery charging protocol](uefi-battery-charging-protocol.md)">UEFI battery charging protocol</a> and <a href="battery-charging-in-the-boot-environment.md" data-raw-source="[Battery charging in the boot environment](battery-charging-in-the-boot-environment.md)">Battery charging in the boot environment</a>.</p>
<div class="alert">
<strong>Important</strong>  This requirement applies only if the device uses the Microsoft UEFI battery charging application. If the device uses a custom UEFI battery charging application instead of the Microsoft-provided application, the UEFI battery charging driver must not implement the UEFI battery charging protocol.
</div>
<div>

</div></td>
</tr>
<tr class="even">
<td>Display power state protocol</td>
<td><p>If the device uses the Microsoft UEFI battery charging application, the UEFI firmware must include a driver that implements the UEFI display power state protocol. This protocol is used to turn the screen and backlight off and on again while charging in the UEFI environment. For more information about this protocol, see <a href="uefi-display-power-state-protocol.md" data-raw-source="[UEFI display power state protocol](uefi-display-power-state-protocol.md)">UEFI display power state protocol</a>. For more information about how this protocol is used by the UEFI battery charging application, see <a href="architecture-of-the-uefi-battery-charging-application.md" data-raw-source="[Architecture of the UEFI battery charging application](architecture-of-the-uefi-battery-charging-application.md)">Architecture of the UEFI battery charging application</a>.</p>
<div class="alert">
<strong>Important</strong>  This requirement applies only if the device uses the Microsoft UEFI battery charging application. If the device uses a custom UEFI battery charging application instead of the Microsoft-provided application, the UEFI battery charging driver must not implement the UEFI display power state protocol.
</div>
<div>

</div></td>
</tr>
<tr class="odd">
<td>Power optimization</td>
<td>It is recommended that the UEFI environment be power-optimized to not use excessive power. This allows the device to use as little power as possible while booting, and to charge as quickly as possible (when charging in UEFI).</td>
</tr>
<tr class="even">
<td>Reserved hardware buttons</td>
<td><p>During the boot process, Microsoft defines standalone presses of the power, volume up and volume down buttons as triggers that can be used to start several Microsoft-provided UEFI applications. OEMs must not overload the power, volume up or volume down button during boot to perform custom actions or start other UEFI applications.</p>
<p>The following list shows which Microsoft-provided UEFI applications are started by these buttons.</p>
<ul>
<li>Volume up: Microsoft-provided UEFI flashing application.</li>
<li>Volume down: Microsoft-provided UEFI device reset application.</li>
<li>Power: Microsoft-provided developer boot menu application.</li>
</ul>
<div class="alert">
<strong>Note</strong><br/><p>OEMs must also ensure that the volume up and volume down buttons function as up arrow and down arrow keys, respectively, in the UEFI environment.</p>
</div>
<div>

</div></td>
</tr>
<tr class="odd">
<td>OEM UEFI applications</td>
<td><p>OEMs can add UEFI applications that aid in manufacturing and servicing the device. These applications have the following restrictions:</p>
<ul>
<li><p>UEFI applications should not affect boot time.</p></li>
<li><p>UEFI applications must be signed with a certificate that is in the allowed signature database (db) UEFI variable.</p></li>
<li><p>UEFI applications must behave in one of the following ways:</p>
<ul>
<li><p>They must <em>never</em> run during a boot to the main OS or update OS.</p>
<p>—or—</p></li>
<li><p>They must <em>always</em> run during the boot to the main OS or update OS.</p></li>
</ul></li>
</ul>
<p>UEFI applications <em>must not</em> sometimes run and sometimes not run during boot to the main OS or update OS. When device encryption is enabled, the trusted platform module (TPM) stores the boot sequence, and it cannot be changed after device encryption is enabled. For example, if the boot sequence is <em>UEFI firmware</em> &gt; <em>application A</em> &gt; bootarm.efi, then removing <em>application A</em> from the boot sequence will cause the TPM to fail to unseal.</p>
<p>In addition, if there are multiple UEFI applications, the firmware should ensure a consistent ordering of the applications. For example, if the boot sequence is <em>UEFI firmware</em> &gt; <em>application A</em> &gt; <em>application B</em> &gt; bootarm.efi, then changing the boot sequence to <em>UEFI firmware</em> &gt; <em>application B</em> &gt; <em>application A</em> &gt; bootarm.efi could cause the TPM to fail to unseal if applications A and B chain to different entries in the db.</p>
<p>Updating the signing certificates of boot applications will not cause a problem with the TPM. However, if UEFI applications are resigned so that they chain to a different entry in the db, then this will also cause the TPM to fail to unseal.</p></td>
</tr>
</tbody>
</table>



## Related topics
[Minimum UEFI requirements for Windows on SoC platforms](minimum-uefi-requirements-for-windows-on-soc-platforms.md)  
[UEFI requirements that apply to all Windows editions](uefi-requirements-that-apply-to-all-windows-platforms.md)  
[UEFI requirements for USB flashing support](uefi-requirements-for-usb-flashing-support.md)  



