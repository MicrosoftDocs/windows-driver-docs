Testing a Driver
============================================================

The WDK adds a driver testing interface to Visual Studio that allows you to conveniently build, deploy, install, and test a driver on a remote test computer on your network. The WDK also provides a collection of device driver tests that you can use to test features and functions of your driver. You can also write customize or write your own driver tests using the Driver Test Template in Visual Studio.

<span id="Video_Demonstration"></span><span id="video_demonstration"></span><span id="VIDEO_DEMONSTRATION"></span>Video Demonstration
-------------------------------------------------------------------------------------------------------------------------------------

This video demonstrates the how to run driver-related tests in a test group.

<iframe 
src="https://hubs-video.ssl.catalog.video.msn.com/embed/e12e5ce5-b41f-4b91-ab5f-69598ccdcb57/IA?csid=ux-en-us&MsnPlayerLeadsWith=html&PlaybackMode=Inline&MsnPlayerDisplayShareBar=false&MsnPlayerDisplayInfoButton=false&iframe=true&QualityOverride=HD" width="720" height="405" allowFullScreen="true" frameBorder="0" scrolling="no"></iframe> 

This section describes some strategies for testing driver, and information about how you select and configure a remote computer to use for testing.

To prepare a driver for public distribution, you should run the [Windows Hardware Certification Kit (HCK)](http://go.microsoft.com/fwlink/p/?linkid=254893). For information about the Windows Certification program and how to obtain the HCK, see [Windows Hardware Certification Program](http://go.microsoft.com/fwlink/p/?linkid=227016).

<span id="in_this_section"></span>In this section
-------------------------------------------------

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<thead>
<tr class="header">
<th align="left">Topic</th>
<th align="left">Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td align="left"><p><a href="strategies_for_testing_drivers_during_development.md">Tips for testing drivers during development</a></p></td>
<td align="left"><p><strong>When should you start testing?</strong> As soon as you have the requirements for your driver, you can begin to design test cases to test that the critical requirements have been implemented. Studies show that finding and fixing defects in code becomes more expensive the longer the defects remain in the code. Finding and fixing defects early in the development cycle is less costly and disruptive than finding defects after the code has been released and distributed. Creating your test cases early can also help you find problems in your design.</p>
<p></p></td>
</tr>
<tr class="even">
<td align="left"><p><a href="testing_a_driver_at_runtime.md">How to test a driver at runtime using Visual Studio</a></p></td>
<td align="left"><p>The WDK extensions to Visual Studio provide a device testing interface that enables you to conveniently build, deploy, install, and test a driver on a test computer on your network. The WDK provides a collection of device driver tests that you can use to test the features and functions of your driver.</p></td>
</tr>
<tr class="odd">
<td align="left"><p><a href="how_to_write_a_driver_test_.md">How to write a driver test using a Driver Test template</a></p></td>
<td align="left"><p>You can use the Windows Driver Kit (WDK) for Windows 8 to create your own driver tests or to customize some of the tests that are provided. You can deploy the tests that you create to remote test computers using the driver testing framework that the WDK provides for Microsoft Visual Studio Ultimate 2012.</p></td>
</tr>
</tbody>
</table>

 

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[VsDriver\vsdriver]:%20Testing%20a%20Driver%20%20RELEASE:%20%289/30/2015%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/en-us/default. "Send comments about this topic to Microsoft")


