---
title: Windows Device Testing Framework (WDTF) design guide
author: windows-driver-content
description: The Microsoft Windows Device Testing Framework (WDTF) enables you to create, manage, reuse, and extend device-centric, scenario-based automated tests.
MSHAttr:
- 'PreferredSiteName:MSDN'
- 'PreferredLib:/library/windows/hardware'
ms.assetid: cff552f0-5dde-4fe7-996c-0a496d845edc
---

# Windows Device Testing Framework (WDTF) design guide


The Microsoft Windows Device Testing Framework (WDTF) enables you to create, manage, reuse, and extend device-centric, scenario-based automated tests.

## In this section


<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<thead>
<tr class="header">
<th>Topic</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><p>[Writing a WDTF SimpleIO plug-in for your device](writing-a-wdtf-simpleio-plug-in-for-your-device.md)</p></td>
<td><p>To get the most benefit from the [Device Fundamental tests](https://msdn.microsoft.com/windows-drivers/develop/how_to_select_and_configure_the_device_fundamental_tests), your device should have a Simple I/O plug-in that can perform simple I/O to your device. This can be one of the default Simple I/O plugs that come with WDTF or one that you wrote. To see if your device type is supported and to determine if there are specific requirements for testing, refer to [Provided WDTF Simple I/O plug-ins](provided-wdtf-simpleio-plug-ins.md).</p></td>
</tr>
<tr class="even">
<td><p>[Writing tests with WDTF](writing-tests-with-wdtf.md)</p></td>
<td><p>Whether you start writing driver tests with the templates provided in the Windows Driver Kit (WDK), or whether you create the tests on your own, the Microsoft Windows Device Testing Framework (WDTF) enables you to create and extend device-centric, scenario-based automated tests.</p></td>
</tr>
<tr class="odd">
<td><p>[Triaging WDTF-based tests](triaging-wdtf-based-tests.md)</p></td>
<td><p>To help you better understand what is going on in your WDTF-based tests, you can use the built-in support for [WDTF Object Logging](logging-and-tracing.md) and [WPP Software Tracing](https://msdn.microsoft.com/library/windows/hardware/ff556204).</p></td>
</tr>
<tr class="even">
<td><p>[WDTF Architecture and Overview](windows-device-testing-framework-design-guide.md)</p></td>
<td><p>The Microsoft Windows Device Testing Framework (WDTF) enables you to create, manage, reuse, and extend device-centric, scenario-based automated tests.</p></td>
</tr>
</tbody>
</table>

 

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bdtf\dtf%5D:%20Windows%20Device%20Testing%20Framework%20%28WDTF%29%20design%20guide%20%20RELEASE:%20%289/13/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


