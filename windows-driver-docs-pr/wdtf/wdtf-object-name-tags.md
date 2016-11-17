---
title: WDTF Object Name tags
author: windows-driver-content
description: The WDTF OBJECT\_NAME tags are used in WDTF object logging.
MSHAttr:
- 'PreferredSiteName:MSDN'
- 'PreferredLib:/library/windows/hardware'
ms.assetid: 25C669DD-12D0-4C78-802F-CB8E26C4FD80
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
<td><p>[<strong>IWDTFTarget2</strong>](https://msdn.microsoft.com/library/windows/hardware/hh439367)</p></td>
<td></td>
</tr>
<tr class="even">
<td><p>WDTF_TARGETS</p></td>
<td><p>[<strong>IWDTFTargets2</strong>](https://msdn.microsoft.com/library/windows/hardware/hh439458)</p></td>
<td><pre class="syntax" space="preserve"><code>Device query 
WDTF_TARGETS              : INFO  :  - Query(&quot;IsDevice AND Volume::BOOT&quot;)
WDTF_TARGETS              : INFO  :          Target: Generic volume (C:) STORAGE\VOLUME\{F1309F19-F052-11DF-BC7C-B1A2109AB6D2}
Get interface 
WDTF_TARGETS              : INFO  :  - GetInterfacesIfExist(&quot;SimpleIOEx&quot;)
WDTF_TARGETS              : INFO  :          Target: Generic volume (C:) STORAGE\VOLUME\{F1309F19-F052-11DF-BC7C-B1A2109AB6D2}</code></pre></td>
</tr>
<tr class="odd">
<td><p>WDTF_SIMPLE_IO</p></td>
<td><p>[<strong>IWDTFSimpleIOEx2</strong>](https://msdn.microsoft.com/library/windows/hardware/hh451149)</p></td>
<td></td>
</tr>
<tr class="even">
<td><p>WDTF_SIMPLEIO_STRESS</p></td>
<td><p>[<strong>IWDTFSimpleIOStressAction2</strong>](https://msdn.microsoft.com/library/windows/hardware/hh451157)</p></td>
<td><pre class="syntax" space="preserve"><code>WDTF_SIMPLEIO_STRESS      : INFO  :  - Start(Generic volume (C:) STORAGE\VOLUME\{2550460D-F167-11E0-B20B-806E6F6E6963}#0000000018100000)
WDTF_SIMPLE_IO            : INFO  :  - Open(Generic volume (C:) STORAGE\VOLUME\{2550460D-F167-11E0-B20B-806E6F6E6963}#0000000018100000) Try count 1
WDTF_SIMPLE_IO            : INFO  :  - PerformIO(Generic volume (C:) STORAGE\VOLUME\{2550460D-F167-11E0-B20B-806E6F6E6963}#0000000018100000) Count 1
WDTF_SIMPLEIO_STRESS      : INFO  :  - Stop(Generic volume (C:) STORAGE\VOLUME\{2550460D-F167-11E0-B20B-806E6F6E6963}#0000000018100000)
WDTF_SIMPLE_IO            : INFO  :  - Close(Generic volume (C:) STORAGE\VOLUME\{2550460D-F167-11E0-B20B-806E6F6E6963}#0000000018100000)

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

 

## <a href="" id="wdtf-system-actions-"></a>WDTF System Actions


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
<td><p>[<strong>IWDTFSystemAction2</strong>](https://msdn.microsoft.com/library/windows/hardware/hh439302)</p></td>
<td></td>
</tr>
<tr class="even">
<td><p>WDTF_TARGETS</p></td>
<td><p>[<strong>IWDTFTargets2</strong>](https://msdn.microsoft.com/library/windows/hardware/hh439458)</p></td>
<td><pre class="syntax" space="preserve"><code>// When reboot and restart is initiated  
WDTF_SYSTEM               : INFO  :  - Reboot and Restart
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

 

## <a href="" id="wdtf-device-actions-"></a>WDTF Device Actions


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
<td><p>[<strong>IWDTFDriverPackageAction2</strong>](https://msdn.microsoft.com/library/windows/hardware/hh406427)</p></td>
<td></td>
</tr>
<tr class="even">
<td><p>WDTF_DRIVER_SETUP_DEVICE</p></td>
<td><p>[<strong>IWDTFDriverSetupAction2</strong>](https://msdn.microsoft.com/library/windows/hardware/hh450938)</p></td>
<td><pre class="syntax" space="preserve"><code>WDTF_DRIVER_SETUP_DEVICE  : INFO  :  - UpdateDriver()
WDTF_DRIVER_SETUP_DEVICE  : INFO  :          Target: TI EHCI controller ACPI\TXI_USBEHCI\2&DABA3FF&2
</code></pre></td>
</tr>
<tr class="odd">
<td><p>WDTF_DRIVER_SETUP_SYSTEM</p></td>
<td><p>[<strong>IWDTFDriverSetupSystemAction2</strong>](https://msdn.microsoft.com/library/windows/hardware/hh450948)</p></td>
<td></td>
</tr>
<tr class="even">
<td><p>WDTF_DRIVER_VERIFIER</p></td>
<td><p>None</p></td>
<td></td>
</tr>
<tr class="odd">
<td><p>WDTF_EDT</p></td>
<td><p>[<strong>IWDTFEnhancedDeviceTestSupportAction2</strong>](https://msdn.microsoft.com/library/windows/hardware/hh450969)</p></td>
<td><pre class="syntax" space="preserve"><code>WDTF_EDT                  : INFO  :  - Enable()   
WDTF_EDT                  : INFO  :          Target: TI EHCI controller ACPI\TXI_USBEHCI\2&DABA3FF&2 
WDTF_EDT                  : INFO  :          Result: System reboot required as device is not disableable  ( 80004005 ).
 
WDTF_EDT                  : INFO  :  - Disable()   
WDTF_EDT                  : INFO  :          Target: OMAP4 Dual-Core ARM Cortex A9 ACPI\TEXAS_INSTRUMENTS_INC._-_ARM_FAMILY_7_MODEL_C09_REVISION_102\0</code></pre></td>
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

 

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bdtf\dtf%5D:%20WDTF%20Object%20Name%20tags%20%20RELEASE:%20%289/13/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


