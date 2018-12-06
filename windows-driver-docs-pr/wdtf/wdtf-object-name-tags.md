---
title: WDTF Object Name tags
description: The WDTF OBJECT_NAME tags are used in WDTF object logging.
ms.assetid: 25C669DD-12D0-4C78-802F-CB8E26C4FD80
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# WDTF Object Name tags


The WDTF OBJECT\_NAME tags are used in WDTF object logging.

## WDTF Core


<table>
<colgroup>
<col width="33%" />
<col width="33%" />
<col width="33%" />
</colgroup>
<thead>
<tr class="header">
<th>Tag name</th>
<th>Interface that uses that tag</th>
<th>Example output</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><p>WDTF_TARGET</p></td>
<td><p><a href="https://msdn.microsoft.com/library/windows/hardware/hh439367" data-raw-source="[&lt;strong&gt;IWDTFTarget2&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/hh439367)"><strong>IWDTFTarget2</strong></a></p></td>
<td></td>
</tr>
<tr class="even">
<td><p>WDTF_TARGETS</p></td>
<td><p><a href="https://msdn.microsoft.com/library/windows/hardware/hh439458" data-raw-source="[&lt;strong&gt;IWDTFTargets2&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/hh439458)"><strong>IWDTFTargets2</strong></a></p></td>
<td><pre class="syntax" space="preserve"><code>Device query 
WDTF_TARGETS              : INFO  :  - Query(&quot;IsDevice AND Volume::BOOT&quot;)
WDTF_TARGETS              : INFO  :          Target: Generic volume (C:) STORAGE\VOLUME{F1309F19-F052-11DF-BC7C-B1A2109AB6D2}
Get interface 
WDTF_TARGETS              : INFO  :  - GetInterfacesIfExist(&quot;SimpleIOEx&quot;)
WDTF_TARGETS              : INFO  :          Target: Generic volume (C:) STORAGE\VOLUME{F1309F19-F052-11DF-BC7C-B1A2109AB6D2}</code></pre></td>
</tr>
<tr class="odd">
<td><p>WDTF_SIMPLE_IO</p></td>
<td><p><a href="https://msdn.microsoft.com/library/windows/hardware/hh451149" data-raw-source="[&lt;strong&gt;IWDTFSimpleIOEx2&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/hh451149)"><strong>IWDTFSimpleIOEx2</strong></a></p></td>
<td></td>
</tr>
<tr class="even">
<td><p>WDTF_SIMPLEIO_STRESS</p></td>
<td><p><a href="https://msdn.microsoft.com/library/windows/hardware/hh451157" data-raw-source="[&lt;strong&gt;IWDTFSimpleIOStressAction2&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/hh451157)"><strong>IWDTFSimpleIOStressAction2</strong></a></p></td>
<td><pre class="syntax" space="preserve"><code>WDTF_SIMPLEIO_STRESS      : INFO  :  - Start(Generic volume (C:) STORAGE\VOLUME{2550460D-F167-11E0-B20B-806E6F6E6963}#0000000018100000)
WDTF_SIMPLE_IO            : INFO  :  - Open(Generic volume (C:) STORAGE\VOLUME{2550460D-F167-11E0-B20B-806E6F6E6963}#0000000018100000) Try count 1
WDTF_SIMPLE_IO            : INFO  :  - PerformIO(Generic volume (C:) STORAGE\VOLUME{2550460D-F167-11E0-B20B-806E6F6E6963}#0000000018100000) Count 1
WDTF_SIMPLEIO_STRESS      : INFO  :  - Stop(Generic volume (C:) STORAGE\VOLUME{2550460D-F167-11E0-B20B-806E6F6E6963}#0000000018100000)
WDTF_SIMPLE_IO            : INFO  :  - Close(Generic volume (C:) STORAGE\VOLUME{2550460D-F167-11E0-B20B-806E6F6E6963}#0000000018100000)

// Note: Start - indicates the device to perform I/O against. 
//       Open -  shows the number of tries that were attempted before the device opened. 

</code></pre></td>
</tr>
<tr class="odd">
<td><p>WDTF_SIMPLEIO_STRESS_PROC</p></td>
<td><p>IWDTFSimpleIOStressProcAction2</p></td>
<td></td>
</tr>
</tbody>
</table>



## WDTF System Actions


<table>
<colgroup>
<col width="33%" />
<col width="33%" />
<col width="33%" />
</colgroup>
<thead>
<tr class="header">
<th>Tag name</th>
<th>Interface that uses that tag</th>
<th>Example output</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><p>WDTF_SYSTEM</p></td>
<td><p><a href="https://msdn.microsoft.com/library/windows/hardware/hh439302" data-raw-source="[&lt;strong&gt;IWDTFSystemAction2&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/hh439302)"><strong>IWDTFSystemAction2</strong></a></p></td>
<td></td>
</tr>
<tr class="even">
<td><p>WDTF_TARGETS</p></td>
<td><p><a href="https://msdn.microsoft.com/library/windows/hardware/hh439458" data-raw-source="[&lt;strong&gt;IWDTFTargets2&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/hh439458)"><strong>IWDTFTargets2</strong></a></p></td>
<td><pre class="syntax" space="preserve"><code>// When reboot and restart is initiated<br/>WDTF_SYSTEM               : INFO  :  - Reboot and Restart
// When we come back 
WDTF_SYSTEM               : INFO  :  - Have restarted. Context = WDTF_RebootRestart
// Sleep cycle 
WDTF_SYSTEM               : INFO  : Attempt Sleep State: 3 , At (hh:mm:ss): 13:7:57 ,  Wake Time In Seconds: 120
WDTF_SYSTEM               : INFO  : Returning from Sleep. Elapsed time (hh:mm:ss): 0:0:53
// Hibernate cycle 
WDTF_SYSTEM               : INFO  : Attempt Hibernate State: 4 , At (hh:mm:ss): 13:8:51 ,  Wake Time In Seconds: 120
WDTF_SYSTEM               : INFO  : Returning from Hibernate. Elapsed time (hh:mm:ss): 0:1:55

// Note: 
// &quot;At (hh:mm:ss)&quot; - Time sleep was initiated 
// &quot;Wake Time In Seconds&quot; - Relative time to wake from sleep 
// &quot;Elapsed time (hh:mm:ss)&quot; - Elapsed time after we returned from sleep 
</code></pre></td>
</tr>
<tr class="odd">
<td><p>WDTF_WDTFSUPPORT</p></td>
<td><p>None</p></td>
<td><pre class="syntax" space="preserve"><code>WDTF_WDTFSUPPORT             : INFO  :  - WaitForSeconds : 3

// Indicates that we waited 3 seconds. </code></pre></td>
</tr>
</tbody>
</table>



## WDTF Device Actions


<table>
<colgroup>
<col width="33%" />
<col width="33%" />
<col width="33%" />
</colgroup>
<thead>
<tr class="header">
<th>Tag name</th>
<th>Interface that uses that tag</th>
<th>Example output</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><p>WDTF_DRIVER_PACKAGE</p></td>
<td><p><a href="https://msdn.microsoft.com/library/windows/hardware/hh406427" data-raw-source="[&lt;strong&gt;IWDTFDriverPackageAction2&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/hh406427)"><strong>IWDTFDriverPackageAction2</strong></a></p></td>
<td></td>
</tr>
<tr class="even">
<td><p>WDTF_DRIVER_SETUP_DEVICE</p></td>
<td><p><a href="https://msdn.microsoft.com/library/windows/hardware/hh450938" data-raw-source="[&lt;strong&gt;IWDTFDriverSetupAction2&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/hh450938)"><strong>IWDTFDriverSetupAction2</strong></a></p></td>
<td><pre class="syntax" space="preserve"><code>WDTF_DRIVER_SETUP_DEVICE  : INFO  :  - UpdateDriver()
WDTF_DRIVER_SETUP_DEVICE  : INFO  :          Target: TI EHCI controller ACPI\TXI_USBEHCI\2&amp;DABA3FF&amp;2
</code></pre></td>
</tr>
<tr class="odd">
<td><p>WDTF_DRIVER_SETUP_SYSTEM</p></td>
<td><p><a href="https://msdn.microsoft.com/library/windows/hardware/hh450948" data-raw-source="[&lt;strong&gt;IWDTFDriverSetupSystemAction2&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/hh450948)"><strong>IWDTFDriverSetupSystemAction2</strong></a></p></td>
<td></td>
</tr>
<tr class="even">
<td><p>WDTF_DRIVER_VERIFIER</p></td>
<td><p>None</p></td>
<td></td>
</tr>
<tr class="odd">
<td><p>WDTF_EDT</p></td>
<td><p><a href="https://msdn.microsoft.com/library/windows/hardware/hh450969" data-raw-source="[&lt;strong&gt;IWDTFEnhancedDeviceTestSupportAction2&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/hh450969)"><strong>IWDTFEnhancedDeviceTestSupportAction2</strong></a></p></td>
<td><pre class="syntax" space="preserve"><code>WDTF_EDT                  : INFO  :  - Enable()<br/>WDTF_EDT                  : INFO  :          Target: TI EHCI controller ACPI\TXI_USBEHCI\2&amp;DABA3FF&amp;2 
WDTF_EDT                  : INFO  :          Result: System reboot required as device is not disableable  ( 80004005 ).

WDTF_EDT                  : INFO  :  - Disable()<br/>WDTF_EDT                  : INFO  :          Target: OMAP4 Dual-Core ARM Cortex A9 ACPI\TEXAS_INSTRUMENTS_INC._-_ARM_FAMILY_7_MODEL_C09_REVISION_102\0</code></pre></td>
</tr>
<tr class="even">
<td><p>WDTF_FUZZTEST</p></td>
<td><p>None</p></td>
<td></td>
</tr>
<tr class="odd">
<td><p>WDTF_FUZZTESTS</p></td>
<td><p>None</p></td>
<td></td>
</tr>
<tr class="even">
<td><p>WDTF_IOATTACK</p></td>
<td><p>None</p></td>
<td></td>
</tr>
<tr class="odd">
<td><p>WDTF_IOSPY</p></td>
<td><p>None</p></td>
<td></td>
</tr>
<tr class="even">
<td><p>WDTF_PNP</p></td>
<td><p>IWDTFPNPAction2</p></td>
<td></td>
</tr>
<tr class="odd">
<td><p>WDTF_CPUUTIL</p></td>
<td><p>None</p></td>
<td><pre class="syntax" space="preserve"><code>WDTF_CPUUTIL              : INFO  :  - SetCpuUtilization : 44% : 0.

// Where the 44% indicates the percent of CPU utilization generated. </code></pre></td>
</tr>
<tr class="even">
<td><p>WDTF_CONCURRENTIO</p></td>
<td><p>None</p></td>
<td></td>
</tr>
<tr class="odd">
<td><p>WDTF_DRIVER_VERIFIER</p></td>
<td><p>None</p></td>
<td></td>
</tr>
</tbody>
</table>



## WDTF Device Simple I/O Actions


<table>
<colgroup>
<col width="33%" />
<col width="33%" />
<col width="33%" />
</colgroup>
<thead>
<tr class="header">
<th>Tag name</th>
<th>Interface that uses that tag</th>
<th>Example output</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><p>WDTF_SIMPLEIO_AUDIO</p></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td><p>WDTF_SIMPLEIO_BLUETOOTH</p></td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td><p>WDTF_ SIMPLEIO_MobileBroadband</p></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td><p>WDTF_SIMPLEIO_SENSOR</p></td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td><p>WDTF_SIMPLEIO_SMARTCARDREADER</p></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td><p>WDTF_SIMPLEIO_UART</p></td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td><p>WDTF_SIMPLEIO_VOLUME</p></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td><p>WDTF_SIMPLEIO_WEBCAM</p></td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td><p>WDTF_SIMPLEIO_WPD</p></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td><p>WDTF_WDTFSUP</p></td>
<td></td>
<td></td>
</tr>
</tbody>
</table>










