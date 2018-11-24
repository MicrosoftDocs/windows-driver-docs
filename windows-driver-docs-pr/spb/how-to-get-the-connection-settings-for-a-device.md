---
title: How to Get the Connection Settings for a Device
description: If your SPB controller driver registers an EvtSpbTargetConnect callback function, the SPB framework extension (SpbCx) calls this function when a client (peripheral driver) of the controller sends an IRP_MJ_CREATE request to open a logical connection to a target device on the bus. In response to the EvtSpbTargetConnect callback, the SPB controller driver should call the SpbTargetGetConnectionParameters method to get the connection settings for the target device. The SPB controller driver stores these settings and uses them later to access the device in response to I/O requests from the client.
ms.assetid: B614993A-0EA9-4B91-A336-80EEF9BE3E69
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# How to Get the Connection Settings for a Device


If your SPB controller driver registers an [*EvtSpbTargetConnect*](https://msdn.microsoft.com/library/windows/hardware/hh450818) callback function, the [SPB framework extension](https://msdn.microsoft.com/library/windows/hardware/hh406203) (SpbCx) calls this function when a client (peripheral driver) of the controller sends an [**IRP\_MJ\_CREATE**](https://msdn.microsoft.com/library/windows/hardware/ff550729) request to open a logical connection to a target device on the bus. In response to the *EvtSpbTargetConnect* callback, the SPB controller driver should call the [**SpbTargetGetConnectionParameters**](https://msdn.microsoft.com/library/windows/hardware/hh450926) method to get the connection settings for the target device. The SPB controller driver stores these settings and uses them later to access the device in response to I/O requests from the client.

For example, the connection settings for a target device on an I2C bus include the bus address of the device, the address width (7 or 10 bits), and the bus clock frequency to use during accesses of the device. The I2C controller driver uses these settings to configure the controller to access the device over the I2C bus.

An SPB controller driver calls **SpbTargetGetConnectionParameters** to get a pointer to a *serial bus connection descriptor* that describes the connection of a target device to a serial bus of type I2C or SPI. This descriptor contains connection information that is common to both serial bus types, and is followed by information that is specific to the serial bus to which the device is connected. For more information about the format for this descriptor, see the [ACPI 5.0 specification](https://www.uefi.org/specifications).

In the following code example, an I2C controller driver defines a **PNP\_I2C\_SERIAL\_BUS\_DESCRIPTOR** structure. This structure represents an *I2C serial bus connection descriptor*, which is the term the ACPI 5.0 specification uses to describe a serial bus connection descriptor that is followed by connection settings that are specific to the I2C bus. The first member of the **PNP\_I2C\_SERIAL\_BUS\_DESCRIPTOR** structure, **SerialBusDescriptor**, is a [**PNP\_SERIAL\_BUS\_DESCRIPTOR**](https://msdn.microsoft.com/library/windows/hardware/jj938062) structure that represents the serial bus connection descriptor. The **ConnectionSpeed** and **SlaveAddress** members contain I2C-specific connection settings.

```cpp
#include <reshub.h>
#include <pshpack1.h>  

//
// See the ACPI 5.0 spec, section 6.4.3.8.2.1 (I2C Serial Bus Connection Descriptor).  
//
typedef struct _PNP_I2C_SERIAL_BUS_DESCRIPTOR {  
    PNP_SERIAL_BUS_DESCRIPTOR SerialBusDescriptor;  
    ULONG ConnectionSpeed;  
    USHORT SlaveAddress;  
    // Followed by optional vendor-specific data.
    // Followed by name of serial bus controller.
} PNP_I2C_SERIAL_BUS_DESCRIPTOR, *PPNP_I2C_SERIAL_BUS_DESCRIPTOR;  
  
#include <poppack.h>
```

The reshub.h header file defines the **PNP\_SERIAL\_BUS\_DESCRIPTOR** structure. The pshpack1.h and poppack.h header files control the structure alignment mode used by the compiler.

An I2C serial bus connection descriptor is a packed data structure in which adjacent fields are aligned to the nearest byte boundaries, without intervening gaps. As a result, a 16-bit integer value in this descriptor might start on an odd byte boundary. In the preceding code example, pshpack1.h is included to tell the compiler to pack adjacent structure members, and poppack.h tells the compiler to resume the default structure alignment.

The **ConnectionSpeed** member of the **PNP\_I2C\_SERIAL\_BUS\_DESCRIPTOR** structure specifies the frequency, in Hertz, at which to clock the I2C bus during accesses of the target device. The **SlaveAddress** member is the bus address of the target device. For some I2C controller drivers, the **SlaveAddress** member might be followed by optional vendor-specific data, but this data is not used by the driver in this code example and is, therefore, not part of the structure definition.

In the following code example, the I2C controller driver from the previous example implements a `GetTargetSettings` routine that calls [**SpbTargetGetConnectionParameters**](https://msdn.microsoft.com/library/windows/hardware/hh450926) to get the connection settings for a target device on the I2C bus. The *Target* input parameter to this routine is a handle to the target device. The *Settings* output parameter is a pointer to a driver-allocated [**SPB\_CONNECTION\_PARAMETERS**](https://msdn.microsoft.com/library/windows/hardware/hh406204) structure to which the routine writes a set of connection parameters. These parameters include a pointer to the requested connection settings.

```cpp
#define I2C_SERIAL_BUS_TYPE 0x01
#define I2C_SERIAL_BUS_SPECIFIC_FLAG_10BIT_ADDRESS 0x0001

typedef enum _I2C_ADDRESS_MODE
{
    AddressMode7Bit,
    AddressMode10Bit
} I2C_ADDRESS_MODE, *PI2C_ADDRESS_MODE;
  
typedef struct _I2C_TARGET_SETTINGS
{
    ULONG  ClockFrequency;
    ULONG  Address;
    I2C_ADDRESS_MODE  AddressMode;
} I2C_TARGET_SETTINGS, *PI2C_TARGET_SETTINGS;

NTSTATUS
GetTargetSettings(_In_ SPBTARGET Target, _Out_ PI2C_TARGET_SETTINGS Settings)
{
    PRH_QUERY_CONNECTION_PROPERTIES_OUTPUT_BUFFER Connection = NULL;
    SPB_CONNECTION_PARAMETERS Params;

    SPB_CONNECTION_PARAMETERS_INIT(&Params);
    SpbTargetGetConnectionParameters(Target, &Params);
    Connection = (PRH_QUERY_CONNECTION_PROPERTIES_OUTPUT_BUFFER)Params.ConnectionParameters;
    if (Connection->PropertiesLength < sizeof(PNP_SERIAL_BUS_DESCRIPTOR))
    {
        return STATUS_INVALID_PARAMETER;
    }

    PPNP_SERIAL_BUS_DESCRIPTOR Descriptor;

    Descriptor = (PPNP_SERIAL_BUS_DESCRIPTOR)Connection->ConnectionProperties;
    if (Descriptor->Tag != SERIAL_BUS_DESCRIPTOR ||
        Descriptor->SerialBusType != I2C_SERIAL_BUS_TYPE)
    {
        return STATUS_INVALID_PARAMETER;
    }

    PPNP_I2C_SERIAL_BUS_DESCRIPTOR I2CDescriptor;
    USHORT I2CFlags;

    I2CDescriptor = (PPNP_I2C_SERIAL_BUS_DESCRIPTOR)Connection->ConnectionProperties;
    Settings->Address = (ULONG)I2CDescriptor->SlaveAddress;
    I2CFlags = I2CDescriptor->SerialBusDescriptor.TypeSpecificFlags;
    Settings->AddressMode = 
                ((I2CFlags & I2C_SERIAL_BUS_SPECIFIC_FLAG_10BIT_ADDRESS) == 0) ? AddressMode7Bit : AddressMode10Bit;

    Settings->ClockFrequency = I2CDescriptor->ConnectionSpeed;

    return STATUS_SUCCESS;
}
```

In the preceding code example, [**SpbTargetGetConnectionParameters**](https://msdn.microsoft.com/library/windows/hardware/hh450926) writes the connection parameters to the driver-allocated `Params` structure. The **ConnectionParameters** member of `Params` points to an [**RH\_QUERY\_CONNECTION\_PROPERTIES\_OUTPUT\_BUFFER**](https://msdn.microsoft.com/library/windows/hardware/jj938063) structure (defined in reshub.h), whose **ConnectionProperties** member is the first byte of the serial bus connection descriptor; the remaining bytes of this descriptor immediately follow the **ConnectionProperties** member. The buffer pointed to by the **ConnectionParameters** member of `Params` is large enough to contain the **RH\_QUERY\_CONNECTION\_PROPERTIES\_OUTPUT\_BUFFER** structure plus the descriptor bytes that follow this structure.

The driver-implemented `GetTargetSettings` routine in the preceding code example performs the following parameter checks on the connection parameters received from **SpbTargetGetConnectionParameters**:

-   Verifies that the size of the serial bus connection descriptor contained in the [**RH\_QUERY\_CONNECTION\_PROPERTIES\_OUTPUT\_BUFFER**](https://msdn.microsoft.com/library/windows/hardware/jj938063) structure is at least **sizeof**(**PNP\_SERIAL\_BUS\_DESCRIPTOR**).
-   Verifies that the first byte of the serial bus connection descriptor is set to SERIAL\_BUS\_DESCRIPTOR (constant value 0x8e), as required by the ACPI 5.0 specification.
-   Verifies that the serial bus type in the serial bus connection descriptor is set to I2C\_SERIAL\_BUS\_TYPE (constant value 0x01), which identifies the serial bus type as I2C.

At the end of the preceding code example, the \*`Settings` structure contains the connection settings (bus address, address width, and bus clock frequency) for the target device. The I2C controller driver uses these connection settings to configure the controller to access the device.

 

 




