---
title: Points to consider regarding threat modeling for drivers
description: This topic discusses points to consider regarding threat modeling for drivers.
ms.assetid: E763A1CB-E440-4D06-89DE-AE8B3B625D34
---

# Points to consider regarding threat modeling for drivers


This topic discusses points to consider regarding threat modeling for drivers.

## <span id="Fast_path_threat_modeling"></span><span id="fast_path_threat_modeling"></span><span id="FAST_PATH_THREAT_MODELING"></span>Fast path threat modeling


If resources are limited, instead of creating a complete threat model diagram, a summary outline can be created to help assess security risks to the driver. For example the text below describes some of the surface areas diagramed in the example driver described in [Create threat models for drivers](create-threat-models-for-drivers.md).

The driver receives data from the operating system in several types of requests:

-   Requests to perform administrative tasks for the driver and its device, through calls to **DriverEntry**, **DriverUnload**, and **AddDevice** routines
-   Plug and Play requests (IRP\_MJ\_PNP)
-   Power management requests (IRP\_MJ\_POWER)
-   Internal device I/O control requests (IRP\_MJ\_INTERNAL\_DEVICE\_CONTROL)

In response to these requests, data flows from the driver back to the operating system as status information. The driver receives data from a user process in the following types of requests:

-   Create, read, and write requests (IRP\_MJ\_CREATE, IRP\_MJ\_READ, or IRP\_MJ\_WRITE)
-   Public device I/O control requests (IRP\_MJ\_DEVICE\_ CONTROL)

In response to these requests, output data and status information flow from the driver back to the user process.

Using this basic understanding of the data flow to your driver, you can examine each input and output area for possible threats.

## <span id="Including_threat_modeling_in_a_broader_Security_Development_Lifecycle__process"></span><span id="including_threat_modeling_in_a_broader_security_development_lifecycle__process"></span><span id="INCLUDING_THREAT_MODELING_IN_A_BROADER_SECURITY_DEVELOPMENT_LIFECYCLE__PROCESS"></span>Including threat modeling in a broader Security Development Lifecycle process


Consider including the threat modeling process in a broader Secure Development Lifecycle - SDL.

The Microsoft SDL process provides a number of recommended software development process that can be modified to fit any size of organization - including a single developer. Consider adding components of the SDL recommendations to your software development process.

For more information, see [Microsoft Security Development Lifecycle (SDL) – Process Guidance](https://msdn.microsoft.com/library/84aed186-1d75-4366-8e61-8d258746bopq.aspx).

**Training and organizational capabilities** - Pursue software development security training to expand your ability to recognize and remediate software vulnerabilities.

Microsoft makes its four core SDL Training classes available for download. [Microsoft Security Development Lifecycle Core Training classes](http://go.microsoft.com/?linkid=9708478)

For more detailed information about SDL training, see this white paper. [Essential Software Security Training for the Microsoft SDL](https://www.microsoft.com/download/details.aspx?id=9950)

**Requirements and design** - The best opportunity to build trusted software is during the initial planning stages of a new release or a new version, because development teams can identify key objects and integrate security and privacy, which minimizes disruption to plans and schedules.

A key output in this phase is to set specific security goals. For example, deciding that all of your code should pass the Visual Studio code analysis "All Rules"with zero warnings.

**Implementation** - All development teams should define and publish a list of approved tools and their associated security checks, such as compiler/linker options and warnings.

For a driver developer most of the useful work is done in this phase. As code is written it is reviewed for possible weakness. Tools such as code analysis and driver verifier are used to look for areas in the code that can be hardened.

**Verification** - Verification is the point at which the software is functionally complete and is tested against security goals outlined in the requirements and design phase.

Additional tools such as binscope and fuzz testers can be used to validate that security design goals have been met and the code is ready to ship

**Release and response** - In preparation for releasing a product, it is desirable to create an incident response plan that describes what you will do to respond to new threats and how you will service the driver after it has shipped. Doing this work in advance will mean that you will be able to respond faster if security issues are identified in code that has shipped.

For more information about the SDL process, see these additional resources:

-   This is the primary Microsoft SDL site and provides an overview of SDL. <http://www.microsoft.com/sdl>

-   This blog describes how to download a free copy of *The Security Development Lifecycle: SDL*, by Michael Howard and Steve Lipner. <https://blogs.msdn.microsoft.com/microsoft_press/2016/04/19/free-ebook-the-security-development-lifecycle/>

-   This page provides links to additional SDL publications. <https://www.microsoft.com/sdl/resources/publications.aspx>

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[hw_design\hw_design]:%20Points%20to%20consider%20regarding%20threat%20modeling%20for%20drivers%20%20RELEASE:%20%286/16/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




