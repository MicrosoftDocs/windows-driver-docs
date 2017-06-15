---
title: Defining and Exporting New GUIDs
author: windows-driver-content
description: Defining and Exporting New GUIDs
MS-HAID:
- 'Other\_2239a4ad-e0b1-41c7-815c-17649f8fc09a.xml'
- 'kernel.defining\_and\_exporting\_new\_guids'
MSHAttr:
- 'PreferredSiteName:MSDN'
- 'PreferredLib:/library/windows/hardware'
ms.assetid: a7deb283-7cab-4f3c-ad96-f8085222456e
keywords: ["globally unique identifiers WDK kernel", "GUIDs WDK kernel", "identifiers WDK GUIDs", "exporting GUIDs"]
---

# Defining and Exporting New GUIDs


## <a href="" id="ddk-defining-and-exporting-new-guids-kg"></a>


You define a new GUID for an item the driver exports to other system components, drivers, or applications. For example, you define a new GUID for a custom PnP event on one of its devices. To define and export a new GUID, you must do the following:

1.  Choose a symbolic name for the GUID.

    Choose a name that represents the purpose of the GUID. For example, the operating system uses such names as GUID\_BUS\_TYPE\_PCI and PARPORT\_WMI\_ALLOCATE\_FREE\_COUNTS\_GUID.

2.  Generate a value for the GUID using Uuidgen.exe or Guidgen.exe. When you install the Microsoft Windows SDK, Uuidgen.exe is automatically installed. Guidgen.exe is available from the [Microsoft Exchange Server GUID Generator](http://go.microsoft.com/fwlink/p/?linkid=121586) download page.

    These utilities generate a unique, formatted string that represents a 128-bit value. The "-s" switch on Uuidgen.exe outputs the GUID formatted as a C structure.

3.  Define the GUID in an appropriate header file.

    Use the **DEFINE\_GUID** macro (defined in Guiddef.h) to associate the GUID symbolic name with its value (see Example 1).

    **Example 1: Defining GUIDs in a GUID-Only Header File**

    ```
    :
     
    DEFINE_GUID( GUID_BUS_TYPE_PCMCIA, 0x09343630L, 0xaf9f, 0x11d0, 
        0x92,0x9f, 0x00, 0xc0, 0x4f, 0xc3, 0x40, 0xb1 );
    DEFINE_GUID( GUID_BUS_TYPE_PCI, 0xc8ebdfb0L, 0xb510, 0x11d0, 
        0x80,0xE9, 0x00, 0x00, 0xf8, 0x1e, 0x1b, 0x30 );
     
    :
    ```

    If the GUID is defined in a header file that contains statements other than GUID definitions, you must take an extra step to ensure that the GUID is instantiated in drivers that include the header file. The **DEFINE\_GUID** statement must occur outside any **\#ifdef** statements that prevent multiple inclusion. Otherwise, if the header file is included in a precompiled header, the GUID will not be instantiated in drivers that use the header file. See Example 2 for a sample GUID definition in a mixed header file.

    **Example 2: Defining GUIDs in a Mixed Header File**

    ```
    #ifndef _NTDDSER_    // this ex. is from a serial driver .h file
    #define _NTDDSER_
     
    :
    // Put other header file definitions here.
    :
     
    #endif  // _NTDDSER_
     
    #ifdef DEFINE_GUID   // Do not break compiles of drivers that 
                         // include this header but that do not
                         // want the GUIDs.
    //
    // Put GUID definitions outside of the multiple inclusion 
    // protection.
     
    DEFINE_GUID(GUID_CLASS_COMPORT, 0x86e0d1e0L, 0x8089, 0x11d0, 0x9c,
        0xe4, 0x08, 0x00, 0x3e, 0x30, 0x1f, 0x73);
     
    DEFINE_GUID (GUID_SERENUM_BUS_ENUMERATOR, 0x4D36E978, 0xE325, 
        0x11CE, 0xBF, 0xC1, 0x08, 0x00, 0x2B, 0xE1, 0x03, 0x18);
     
    :
    #endif  // DEFINE_GUID
    ```

    Putting a GUID definition outside statements that prevent multiple inclusion does not cause multiple instances of the GUID in a driver because **DEFINE\_GUID** defines the GUID as an EXTERN\_C variable. Multiple declarations of an EXTERN variable are allowed as long as the types match.

4.  When creating a GUID for a new [device setup class](https://msdn.microsoft.com/library/windows/hardware/ff541509) or [device interface class](https://msdn.microsoft.com/library/windows/hardware/ff541339), the following rules apply:
    -   Do not use a single GUID to identify both a device setup class and a device interface class.

    -   When creating a symbolic name to associate with the GUID, use the following convention:

        For device setup classes, use the format GUID\_DEVCLASS\_*XXX*.

        For device interface classes, use the format GUID\_DEVINTERFACE\_*XXX*.

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bkernel\kernel%5D:%20Defining%20and%20Exporting%20New%20GUIDs%20%20RELEASE:%20%286/14/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


