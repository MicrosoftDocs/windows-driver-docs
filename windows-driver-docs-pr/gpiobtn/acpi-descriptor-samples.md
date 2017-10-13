---
title: ACPI descriptor samples
author: windows-driver-content
description: This topic contains ACPI descriptor samples.
ms.assetid: E091DF59-2E9F-4652-801C-3F55CBB910FE
---

# ACPI descriptor samples


This topic contains ACPI descriptor samples.

**Note**  Use only 4 chars length for ACPI descriptors for device definitions (such as CONV).

 

## <span id="ACPI_description_for_button_array"></span><span id="acpi_description_for_button_array"></span><span id="ACPI_DESCRIPTION_FOR_BUTTON_ARRAY"></span>ACPI description for button array


``` syntax
Device(BTT00N)
{
    Method(_HID, 0x0, NotSerialized)
    {
        Return("ID9000")
    }
        Name(_CID, "PNP0C40")
        Name(_CRS, ResourceTemplate()
                {
                GpioInt(Edge, 
                        ActiveLow, 
                        SharedAndWake, 
                        PullDefault, 
                        0, "\\_SB.GPIO", 
                        0, ResourceConsumer, , 
                        RawDataBuffer() {}) 
                 {0xE1}
                GpioInt(Edge, 
                        ActiveBoth, 
                        SharedAndWake, 
                        PullDefault, 
                        0, "\\_SB.GPIO", 
                        0, ResourceConsumer, , 
                        RawDataBuffer() {}) 
                {0xE2}
                GpioInt(Edge, 
                        ActiveBoth, 
                        Exclusive, 
                        PullDefault, 
                        0, "\\_SB.GPIO", 
                        0, ResourceConsumer, , 
                        RawDataBuffer() {}) 
                {0xE3}
                GpioInt(Edge, 
                        ActiveBoth, 
                        Exclusive, 
                        PullDefault, 
                        0, "\\_SB.GPIO", 
                        0, ResourceConsumer, , 
                        RawDataBuffer() {}) 
                {0xE4}
                GpioInt(Edge, 
                        ActiveBoth, 
                        Exclusive, 
                        PullDefault, 
                        0, "\\_SB.GPIO", 
                        0, ResourceConsumer, , 
                        RawDataBuffer() {}) 
                {0xE5}
                })
}
```

## <span id="ACPI_description_for_laptop_slate_mode_indicator"></span><span id="acpi_description_for_laptop_slate_mode_indicator"></span><span id="ACPI_DESCRIPTION_FOR_LAPTOP_SLATE_MODE_INDICATOR"></span>ACPI description for laptop/slate mode indicator


``` syntax
Device(CONV)
{
    Method(_HID, 0x0, NotSerialized)
        {
            Return("ID9001")
        }
     Name(_CID, "PNP0C60")
}
```

## <span id="ACPI_description_for_docking_mode_indicator"></span><span id="acpi_description_for_docking_mode_indicator"></span><span id="ACPI_DESCRIPTION_FOR_DOCKING_MODE_INDICATOR"></span>ACPI description for docking mode indicator


``` syntax
Device(DOCK)
{
    Method(_HID, 0x0, NotSerialized)
    {
        Return("ID9002")
     }
     Name(_CID, "PNP0C70")
}
```

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[gpiobtn\gpiobtn]:%20ACPI%20descriptor%20samples%20%20RELEASE:%20%289/25/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


