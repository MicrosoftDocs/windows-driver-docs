---
title: SCSI Verification
description: SCSI Verification
ms.assetid: dba63137-ff92-480a-bca4-ab651a6bda85
keywords:
- SCSI Verification feature WDK Driver Verifier
- miniport drivers WDK Driver Verifier
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# SCSI Verification


## <span id="ddk_scsi_verification_tools"></span><span id="DDK_SCSI_VERIFICATION_TOOLS"></span>


The SCSI Verification feature of Driver Verifier monitors the interaction between a SCSI miniport driver and the port driver. If the miniport driver misuses a routine, responds incorrectly to a request from the port driver, or takes an excessive amount of time to respond to a request, a bug check is issued.

This Driver Verifier option is only available in Windows XP and later.

### <span id="violations_detected_by_scsi_verification"></span><span id="VIOLATIONS_DETECTED_BY_SCSI_VERIFICATION"></span>Violations Detected by SCSI Verification

The SCSI Verification option can detect several misuses of SCSI routines. It is also possible to individually disable certain of these checks.

When a SCSI miniport driver commits one of the following violations, Driver Verifier will issue bug check 0xF1.

-   The miniport driver passes a bad argument to **ScsiPortInitialize**.

-   The miniport driver calls **ScsiPortStallExecution** and specifies a delay longer than 0.1 second, stalling the processor for an excessive length of time.

-   The port driver calls a miniport driver routine, and the miniport driver takes longer than 0.5 second to execute it. (The **FindAdapter** routine is exempt, and the **HwInitialize** routine is allowed 5 seconds.)

-   The miniport driver completes a request more than once.

-   The miniport driver completes a routine with an invalid SRB status.

-   The miniport driver calls **ScsiPortNotification** to ask for **NextLuRequest**, but an untagged request is still active.

-   The miniport driver passes an invalid virtual address to **ScsiPortGetPhysicalAddress**. (This usually means the address supplied doesn't map to the common buffer area.)

-   The bus reset hold period ends, but the miniport driver still has outstanding requests.

See [**Bug Check 0xF1**](https://msdn.microsoft.com/library/windows/hardware/ff560365) (SCSI\_VERIFIER\_DETECTED\_VIOLATION) for a complete list of the bug check parameters.

In addition to these violations, SCSI Verification also monitors the miniport driver's memory access for improper use. Two common memory violations made by miniport drivers are accessing an SRB extension after a request completes, and accessing an SRB's **DataBuffer** when the miniport driver has not specified **MapBuffers**.

Memory violations of this sort will usually result in [**Bug Check 0xD1**](https://msdn.microsoft.com/library/windows/hardware/ff560244) (DRIVER\_IRQL\_NOT\_LESS\_OR\_EQUAL) being issued.

### <span id="activating_this_option"></span><span id="ACTIVATING_THIS_OPTION"></span>Activating This Option

The procedure for activating the SCSI Verification option is different from the procedures for activating other Driver Verifier options.

**To activate SCSI Verification**

1.  Using Driver Verifier Manager or the Verifier.exe command line, start a verification of the miniport driver. Because SCSI Verification will not be available as an option, you must select at least one other Driver Verifier option. See [Selecting Driver Verifier Options](selecting-driver-verifier-options.md) and [Selecting Drivers to be Verified](selecting-drivers-to-be-verified.md) for details.

2.  Open the registry using regedit.exe. In the **HKEY\_LOCAL\_MACHINE\\SYSTEM\\CurrentControlSet\\Control\\ScsiPort** key, add a subkey named **Verifier**. Within that key, add a REG\_DWORD entry named **VerifyLevel**. The value assigned to this entry will determine which SCSI Verification tests will be active. The value 0x1 will give maximum verification.

3.  Reboot the computer.

If the **VerifyLevel** value does not exist, or is equal to 0xFFFFFFFF, SCSI Verification will be disabled.

The individual bits in the **VerifyLevel** value can be used to control exactly which tests will be performed. Bit zero (0x1) enables certain tests; bits 28, 29, 30, and 31 disable certain tests. Therefore, maximum verification can be obtained by using the value 0x00000001.

The effects of each bit are as follows:

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
<th align="left">Effect</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td align="left"><p>0</p></td>
<td align="left"><p>0x1</p></td>
<td align="left"><p>Driver Verifier will monitor the miniport driver&#39;s memory access and check for improper use of memory buffers.</p></td>
</tr>
<tr class="even">
<td align="left"><p>28</p></td>
<td align="left"><p>0x10000000</p></td>
<td align="left"><p>Driver Verifier will not issue a bug check when the <strong>HwAdapterControl</strong> routine takes more than 0.5 second to complete.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>29</p></td>
<td align="left"><p>0x20000000</p></td>
<td align="left"><p>Driver Verifier will not issue a bug check when a reset hold period ends and there are still outstanding requests on a logical unit.</p></td>
</tr>
<tr class="even">
<td align="left"><p>30</p></td>
<td align="left"><p>0x40000000</p></td>
<td align="left"><p>Driver Verifier will not issue a bug check when the miniport driver calls <strong>ScsiPortNotification</strong> with <strong>NextLuRequest</strong> while an untagged request is still active.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>31</p></td>
<td align="left"><p>0x80000000</p></td>
<td align="left"><p>Driver Verifier will not issue a bug check when the <strong>HwInitialize</strong> routine takes more than 5 seconds to complete.</p></td>
</tr>
</tbody>
</table>

 

In most cases, the recommended setting is 0xD0000001. This enables all **SCSI Verifier** tests except for the time limit on **HwAdapterControl**, the time limit on **HwInitialize**, and the ban on multiple requests to a logical unit. These three tests are often too stringent.

If a kernel debugger is attached, it is possible to change the SCSI Verification level after the boot cycle. To do this, use the debugger command:

```
kd> ed scsiport!SpVrfyLevel Level 
```

This command allows you to set a new value for *Level*. Using this method, you can change the high bits (0x10000000 through 0x8000000) at any time. However, if you wish to change the low bit (0x1), you must do so during the boot process (at the kernel debugger's initial breakpoint).

Similarly, if you want to completely deactivate SCSI Verification, you need to set *Level* to 0xFFFFFFFF at the initial breakpoint.

**Note**   The value 0xF0000000 will disable all tests, but the SCSI Verification modules will still be loaded. Use this value if you wish to disable verification but intend to enable the high-bit tests at a later time. On the other hand, the value 0xFFFFFFFF prevents the modules from being loaded entirely; if this value is used during boot it will not be possible to enable SCSI Verification without rebooting.

 

### <span id="activating_without_rebooting"></span><span id="ACTIVATING_WITHOUT_REBOOTING"></span>Activating without Rebooting

In general, you cannot activate or deactivate SCSI Verification without restarting ("rebooting") the computer on any Windows operating system. The ScsiPort.sys driver reads the **VerifyLevel** registry entry only when it loads, which is typically at boot time. However, if the ScsiPort.sys driver is not loaded when you add the registry entry, or if it is unloaded and reloaded, you can enable SCSI Verification on Windows XP and later versions of Windows without restarting the computer.

 

 





