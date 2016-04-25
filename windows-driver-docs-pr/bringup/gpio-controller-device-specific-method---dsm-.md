---
title: GPIO controller Device-Specific Method (\_DSM)
description: To support a variety of device-class-specific communications between the general-purpose I/O (GPIO) driver stack in Windows and the platform firmware, Microsoft defines a Device-Specific Method (\_DSM) that can be included under a GPIO controller in the ACPI namespace.
MSHAttr:
- 'PreferredSiteName:MSDN'
- 'PreferredLib:/library/windows/hardware'
ms.assetid: 2891A78C-8C4F-4FE4-AB69-402F04DFA885
---

# GPIO controller Device-Specific Method (\_DSM)


To support a variety of device-class-specific communications between the general-purpose I/O (GPIO) driver stack in Windows and the platform firmware, Microsoft defines a Device-Specific Method (\_DSM) that can be included under a GPIO controller in the ACPI namespace.

Currently, this method defines two functions:

-   **Function Index 0**: The Standard Query Function that all \_DSM methods are required to provide.
-   **Function Index 1**: The ActiveBoth Polarity Function, which informs the GPIO stack of any ActiveBoth pins on the controller that are not asserted logic low. The GPIO stack assumes that ActiveBoth pins are asserted logic low, so this function allows the platform to override that default for specific pins.

## GUID definition


The GUID for the GPIO controller \_DSM method is defined to be:

`{4F248F40-D5E2-499F-834C-27758EA1CD3F}`

## Function 0


Function 0 of every \_DSM is a query function that returns the set of supported function indexes, and is always required. For the definition of Function 0, see section 9.14.1, "\_DSM (Device Specific Method)", in the [ACPI 5.0 specification](http://www.acpi.info).

## Function 1


The parameters for Function 1 of the GPIO controller \_DSM method are defined as follows:

### Arguments

-   **Arg0:** UUID for GPIO controller \_DSM

    `// GUID: {4F248F40-D5E2-499F-834C-27758EA1CD3F}`

    `DEFINE_GUID (GPIO_CONTROLLER _DSM_GUID,`

    `0x4f248f40, 0xd5e2, 0x499f, 0x83, 0x4c, 0x27, 0x75, 0x8e, 0xa1, 0xcd. 0x3f);`

-   **Arg1:** Revision ID

    `#define GPIO_CONTROLLER _DSM_REVISION_ID     0`

-   **Arg2:** Function index for ActiveBoth asserted polarity:

    `#define GPIO_CONTROLLER_DSM_ACTIVE_BOTH_POLARITY_FUNCTION_INDEX  1`

-   **Arg3:** Package empty (not used)

### Return

A package of integers, each of which is the controller-relative pin number of a pin on the GPIO controller that is:

-   Defined to be an ActiveBoth interrupt, and
-   Whose asserted state is *not* logic low (in other words, *is* logic high).

For example, if an emulated ActiveBoth pin is connected to a pushbutton device, the pin enters the *asserted* state (logic-high input level at pin) when the user presses the button, and stays in the asserted state while the user holds the button down. When the user releases the button, the pin state changes to *unasserted* (logic-low input level).

## ASL code example


The following ASL code example identifies a set of GPIO pins that have initial polarity of ActiveHigh.

```
//
// _DSM - Device-Specific Method
//
// Arg0:    UUID       Unique function identifier
// Arg1:    Integer    Revision Level
// Arg2:    Integer    Function Index (0 = Return Supported Functions)
// Arg3:    Package    Parameters
//

Function(_DSM,{BuffObj, PkgObj, IntObj},{BuffObj, IntObj, IntObj, PkgObj})
{

    //
    // Switch based on which unique function identifier was passed in
    //

    //
    // GPIO CLX UUID
    //

    If(LEqual(Arg0,ToUUID("4F248F40-D5E2-499F-834C-27758EA1CD3F")))
    {
        switch(Arg2)
        {

            //
            // Function 0: Return supported functions, based on 
            //    revision
            //

            case(0)
            {
                // Revision 0+: Functions 0 &amp; 1 are supported
                return (Buffer() {0x3})
            }

            //
            // Function 1: For emulated ActiveBoth controllers, 
            //    returns a package of controller-relative pin
            //    numbers. Each corresponding pin will have an
            //    initial polarity of ActiveHigh.
            //
            //    A pin number of 0xffff is ignored.
            //

            case(1)
            {     
                // Marks pins 0x28, 0x29 and 0x44 to be ActiveHigh.
                Return (Package() {0x28, 0x29, 0x44})
            }

            //
            // Unrecognized function for this revision
            //

            default
            {
                BreakPoint
            }
        }
    }
    else
    {
        //
        // If this is not one of the UUIDs we recognize, then return
        // a buffer with bit 0 set to 0 to indicate that no functions
        // are supported for this UUID.
        //

        return (Buffer() {0})
    }
}
```

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bp_OEMBringUp\p_oembringup%5D:%20GPIO%20controller%20Device-Specific%20Method%20%28_DSM%29%20%20RELEASE:%20%284/22/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




