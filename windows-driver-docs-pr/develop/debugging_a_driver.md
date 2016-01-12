Debugging a Driver
================================================================

Typically, debugging a kernel-mode driver requires two computers. The debugger runs on the *host computer*, and the code being debugged runs on the *target computer*. The target computer is also called the *test computer*. You can debug a user-mode driver on the host computer or on a separate target computer. Before you can debug a driver running on a target computer, you must configure the target computer for debugging.

For information about configuring a target computer and setting up a debug cable, see [Setting Up Kernel-Mode Debugging in Visual Studio](https://msdn.microsoft.com/en-us/windows/hardware/hh439376) and [Provision a computer for driver deployment and testing (WDK 8.1)](https://msdn.microsoft.com/en-us/Library/Windows/Hardware/Dn745909).

For information about using Microsoft Visual Studio to debug a driver, see [Debugging Using Visual Studio](https://msdn.microsoft.com/en-us/Library/Windows/Hardware/Hh406281).

For an example of using Visual Studio to debug a kernel-mode driver, see [Writing a KMDF driver based on a template](https://msdn.microsoft.com/en-us/Library/Windows/Hardware/Hh439654).

For an introduction to Debugging Tools for Windows, see [Windows Debugging](https://msdn.microsoft.com/en-us/Library/Windows/Hardware/Ff551063).

<span id="Video_Demonstration"></span><span id="video_demonstration"></span><span id="VIDEO_DEMONSTRATION"></span>Video Demonstration
-------------------------------------------------------------------------------------------------------------------------------------

This video demonstrates how to use the WinDbg debugging engine directly in Visual Studio instead of running WinDbg separately.

<iframe 
src="https://hubs-video.ssl.catalog.video.msn.com/embed/57464a96-8900-4194-b806-813eb1dd6ac6/IA?csid=ux-en-us&MsnPlayerLeadsWith=html&PlaybackMode=Inline&MsnPlayerDisplayShareBar=false&MsnPlayerDisplayInfoButton=false&iframe=true&QualityOverride=HD" width="720" height="405" allowFullScreen="true" frameBorder="0" scrolling="no"></iframe> 
 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[VsDriver\vsdriver]:%20Debugging%20a%20Driver%20%20RELEASE:%20%289/30/2015%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/en-us/default. "Send comments about this topic to Microsoft")


