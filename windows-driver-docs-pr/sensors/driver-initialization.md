---
title: Driver initialization
description: Driver initialization
ms.assetid: 9886BBBC-7EE5-45AF-AEDD-75C0885C622B
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Driver initialization


Driver initialization is one of the more complex phases of a user-mode driver’s functionality. It touches most, if not all, of the components in the sample driver.

### ACPI configuration and initialization

| Module               | Class/Interface |
|----------------------|-----------------|
| SpbAccelerometer.asl | N/A             |

 

The sample driver is designed so that the sensor is permanently connected to an I2C bus. Instead of supporting Plug and Play, it supports the Advanced Configuration and Power Interface (ACPI).

ACPI allows Windows to control a device’s configuration and power management. The ACPI spec has definitions for tables that link your Windows device and peripheral devices connected to the system board. The Differentiated System Description Table (DSDT) describes peripheral devices connected to the system—including sensors. It’s stored in a binary format known as the ACPI Machine Language (AML). For more information about the DSDT table, see to the ACPI system description tables topic. (Note that some systems also use the Secondary System Description Table (SSDT) to describe peripheral devices.)

To install a sensor device and driver on your Windows SoC device, you’ll need to update the DSDT table with a corresponding node. This node has information about the sample device’s controllers and connectors. Here’s how Windows and your driver use the data in the node:

1.  1. The Plug and Play (PnP) manager gets device connection information from the ACPI driver.
2.  The PnP manager then creates a connection ID to represent the bus connection.
3.  The PnP manager passes the connection ID to the sample driver as a hardware resource.
4.  The sample driver uses the connection ID to open a logical connection to the sensor device, and gets a handle to the connection.
5.  The driver specifies this handle as the target for I/O requests that it sends to the device.

### Updating the DSDT table

For instructions explaining how to update the DSDT table, refer to the [Install the sample device and driver on your Sharks Cove](installing-the-sample-device-and-driver-on-your-sharks-cove-board.md) topic.

### Modifying the sample ASL file

If you modify the sample driver to support another device, you’ll make corresponding updates to the sample ASL file. Most of your updates will be to the \_CRS section of the file where you specify the I2C and GPIO resources your device needs. You’ll also need to provide a unique \_HID entry that matches the corresponding entry in your updated INF file.

### Decoding I2C or GPIO resources

If you do not specify the /resdecode option, the \_CRS section will contain a binary blob. To convert this section to human-readable text, apply /resdecode as shown below: Asl.exe /tab:dsdt /resdecode

### Updating the Windows setup-information file

| Module               | Class/Interface |
|----------------------|-----------------|
| SpbAccelerometer.inf | N/A             |

 

In addition to updating the DSDT table, you’ll need to update the Windows setup information file (INF) to specify that your device supports ACPI. Because the sensor is always enumerated by ACPI, the hardware identifier in the INF file must contain the “ACPI” string.

```cpp
; =================== Manufacturer/Models sections =======================

[Manufacturer]
%MSFT%                      = Microsoft,NTx86

[Microsoft.NTx86]
%SpbAccelerometer.DeviceDesc% = SpbAccelerometer_Install,ACPI\SpbAccelerometer
```

### Initializing the driver and device

| Module      | Class/Interface |
|-------------|-----------------|
| DllMain.cpp | N/A             |
| Device.cpp  | CMyDevice       |
| Driver.cpp  | CMyDriver       |
| Queue.cpp   | CMyQueue        |

 

The methods below are invoked by Windows or by the driver during the early initialization phase. The preliminary device-initialization methods apply to any device supported by your driver. They appear in the module Device.cpp.

|     | Method                        | Invoked By                                                         | Purpose                                                                                                       |
|-----|-------------------------------|--------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------|
| 1   | **DllGetClassObject**         | WUDFHost.exe                                                       | Gets the driver’s class object. (Required for any COM DLL.)                                                   |
| 2   | **CMyDevice::OnQueryRemove**  | WUDFx.dll (a component of the Windows user-mode driver framework). |                                                                                                               |
| 3   | **CMyDriver::OnDeviceAdd**    | WUDFx.dll (a component of the Windows user-mode driver framework). | Notifies the driver that a device has been added.                                                             |
| 4   | **CMyDevice::Configure**      | **CMyDriver::OnDeviceAdd**                                         | Configures the device’s queues and the corresponding callback objects.                                        |
| 5   | **CMyQueue:CreateInstance**   | **CMyDevice::Configure**                                           | Creates an instance of the device’s queue callback                                                            |
| 6   | **CMyDevice::CreateInstance** | **CMyDevice::OnDeviceAdd**                                         | Creates an instance of the device object that corresponds to a given device (in this case the accelerometer). |
| 7   | **CMyDevice::Initialize**     | **CMyDevice::CreateInstance**                                      | Initializes the device callback object.                                                                       |

 

### Establishing a data connection

| Module                  | Class/Interface      |
|-------------------------|----------------------|
| Device.cpp              | CMyDevice            |
| SensorDdi.cpp           | CSensorDdi           |
| AccelerometerDevice.cpp | CAccelerometerDevice |

 

The methods below are invoked by the driver during initialization to prepare the device objects, get the ACPI configuration data, and create the data-connection interrupt. For the sample driver, these methods are found in the file AccelerometerDevice.cpp.

If you’re porting the sample driver to support another device, such as a compass, you’ll create a parallel module, CompassDevice.cpp. Replace the CAccelerometerDevice class with a CCompassDevice class and revise the methods in the sample’s module to support your device’s objects, data, and interrupt.

|     | Method                                                 | Invoked by                                                         | Purpose                                                                                                                |
|-----|--------------------------------------------------------|--------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------|
| 1   | **CMyDevice::OnPrepareHardware**                       | WUDFx.dll (a component of the Windows user-mode driver framework). | Start the operations required to make the given device accessible by the driver.                                       |
| 2   | **CSensorDdi::Initialize**                             | **CMyDevice::OnPrepareHardware**                                   | Create and initialize the sensor device object.                                                                        |
| 3   | **CSensorDevice::Initialize**                          | **CSensorDdi::Initialize**                                         | Initializes the sensor driver interface, the client manager, and the report manager.                                   |
| 4   | **CAccelerometerDevice::InitializeDevice**             | **CSensorDevice::Initialize**                                      | Initializes the accelerometer device object.                                                                           |
| 5   | **CAccelerometerDevice::GetConfigurationData**         | **CAccelerometerDevice::InitializeDevice**                         | Initiates the retrieval of configuration data from ACPI.                                                               |
| 6   | **CAccelerometerDevice::PrepareInputParametersForDsm** | **CAccelerometerDevice::GetConfigurationData**                     | Prepares an ACPI input buffer (ACPI\_EVAL\_INPUT\_BUFFER) prior to invoking the Device Specific Method (DSM) function. |
| 7   | **CAccelerometerDevice::ParseAcpiOutputBuffer**        | **CAccelerometerDevice::GetConfigurationData**                     | Parses the configuration data that was returned in the ACPI output buffer (ACPI\_EVAL\_OUTPUT\_BUFFER).                |
| 8   | **CAccelerometerDevice::ParseResources**               | **CAccelerometerDevice::InitializeDevice**                         | Parses the device resources to ensure that they support serial I2C connections.                                        |
| 9   | **CAccelerometerDevice::ConnectInterrupt**             | **CAccelerometerDevice::ParseResources**                           | Creates the data-connection interrupt.                                                                                 |

 

### Initializing the SPB request object

| Module                  | Class/Interface      |
|-------------------------|----------------------|
| Device.cpp              | CMyDevice            |
| SensorDdi.cpp           | CSensorDdi           |
| AccelerometerDevice.cpp | CAccelerometerDevice |
| SpbRequest.cpp          | CSpbRequest          |

 

The methods below are invoked by the driver during initialization to open a file handle to the underlying SPB controller. (Note that the first four methods of this sequence are the same as the first four methods in the data-connection sequence.)

|     | Method                                      | Invoked by                                                         | Purpose                                                                                                                                          |
|-----|---------------------------------------------|--------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------|
| 1   | **CMyDevice::OnPrepareHardware**            | WUDFx.dll (a component of the Windows user-mode driver framework). | Starts the operations required to make the given device accessible by the driver.                                                                |
| 2   | **CSensorDdi::Initialize**                  | **CMyDevice::OnPrepareHardware**                                   | Creates and initializes the sensor device object.                                                                                                |
| 3   | **CSensorDevice::Initialize**               | **CSensorDdi::Initialize**                                         | Initializes the sensor driver interface, the client manager, and the report manager.                                                             |
| 4   | **CAccelerometerDevice::InitializeDevice**  | **CSensorDevice::Initialize**                                      | Initializes the accelerometer device object.                                                                                                     |
| 5   | **CAccelerometerDevice::InitializeRequest** | **CAccelerometerDevice::InitializeDevice**                         | Starts the initialization process for the SPB request object (using the resource hub path and connection ID which the driver retrieved earlier). |
| 6   | **CSpbRequest::Initialize**                 | **CAccelerometerDevice::InitializeRequest**                        | Opens a file handle to the underlying SPB                                                                                                        |

 

### Initializing the supported sensor properties and data fields

| Module                  | Class/Interface      |
|-------------------------|----------------------|
| Device.cpp              | CMyDevice            |
| SensorDdi.cpp           | CSensorDdi           |
| AccelerometerDevice.cpp | CAccelerometerDevice |
| SpbRequest.cpp          | CSpbRequest          |

 

The methods below are invoked by the driver during initialization to get the properties and data fields supported by the sensor. For the Windows sensor platform, the accelerometer properties correspond to read or read-write data, such as the sensor’s report interval or its minimum supported report interval. The data fields correspond to the actual accelerometer readings along its X-, Y-, and Z-axis. (Note that the first three methods of this sequence are the same as the first three methods in the previous data-connection, and SPB request-object, sequences.)

|     | Method                                             | Invoked by                                                         | Purpose                                                                                                               |
|-----|----------------------------------------------------|--------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------|
| 1   | **CMyDevice::OnPrepareHardware**                   | WUDFx.dll (a component of the Windows user-mode driver framework). | Starts the operations required to make the given device accessible by the driver.                                     |
| 2   | **CSensorDdi::Initialize**                         | **CMyDevice::OnPrepareHardware**                                   | Creates and initialize the sensor device object.                                                                      |
| 3   | **CSensorDevice::Initialize**                      | **CSensorDdi::Initialize**                                         | Initializes the sensor driver interface, the client manager, and the report manager.                                  |
| 4   | **CSensorDevice::InitializeSensorDriverInterface** | **CSensorDevice::Initialize**                                      | Starts the initialization of the **IPortableDeviceValues** objects that store the property keys and datafield values. |
| 5   | **CSensorDevice::AddPropertyKeys**                 | **CSensorDevice::InitializeSensorDriverInterface**                 | Iterates through the supported properties and adds a **PROPERTYKEY** for each.                                        |
| 6   | **CAccelerometerDevice::GetSupportedProperties**   | **CSensorDevice::AddPropertyKeys**                                 | Gets the **PROPERTYKEY** structures for the given device’s properties.                                                |
| 7   | **CSensorDevice::AddDataFieldKeys**                | **CSensorDevice::InitializeSensorDriverInterface**                 | Iterates through the supported data fields and adds a **PROPERTYKEY** for each.                                       |
| 8   | **CSensorDevice::GetSupportedDataFields**          | **CSensorDevice::AddDataFieldKeys**                                | Gets the **PROPERTYKEY**s for the given device’s data fields.                                                         |

 

### Initializing the persistent unique ID property

| Module                  | Class/Interface      |
|-------------------------|----------------------|
| Device.cpp              | CMyDevice            |
| SensorDdi.cpp           | CSensorDdi           |
| AccelerometerDevice.cpp | CAccelerometerDevice |
| SensorDevice.cpp        | CSensorDevice        |

 

The methods below are invoked by the driver during initialization to initialize the persistent unique identifier (PUID) for the sensor. Windows uses the **PUID** to persist data across device sessions. (Note that the first four methods of this sequence are the same as the first four methods in the previous property and data-field sequence.)

|     | Method                                             | Invoked by                                                         | Purpose                                                                                                   |
|-----|----------------------------------------------------|--------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------|
| 1   | **CMyDevice::OnPrepareHardware**                   | WUDFx.dll (a component of the Windows user-mode driver framework). | Starts the operations required to make the given device accessible by the driver.                         |
| 2   | **CSensorDdi::Initialize**                         | **CMyDevice::OnPrepareHardware**                                   | Creates and initialize the sensor device object.                                                          |
| 3   | **CSensorDevice::Initialize**                      | **CSensorDdi::Initialize**                                         | Initializes the sensor driver interface, the client manager, and the report manager.                      |
| 4   | **CSensorDevice::InitializeSensorDriverInterface** | **CSensorDevice::Initialize**                                      | Starts the initialization of the objects that store the property keys and datafield values.               |
| 5   | **CSensorDevice::SetUniqueID**                     | **CSensorDevice::InitializeSensorDriverInterface**                 | Invokes a method that gets a persistent unique identifier (PUID) that the driver can use across sessions. |
| 6   | **CAcclerometerDevice::GetSensorObjectID**         | **CSensorDevice::SetUniqueID**                                     | Gets the accelerometer’s persistent identifier (“ADXL345”).                                               |

 

### Setting the default property values

| Module                  | Class/Interface      |
|-------------------------|----------------------|
| Device.cpp              | CMyDevice            |
| SensorDdi.cpp           | CSensorDdi           |
| AccelerometerDevice.cpp | CAccelerometerDevice |
| SensorDevice.cpp        | CSensorDevice        |

 

The Windows sensor platform supports default property values for sensor type, manufacturer’s name, sensor model, and serial number. The code in the SpbAccelerometer sample sets these properties as part of the driver and device initialization phase. The methods below are invoked by the driver, during initialization, to set the default values for the accelerometer. (Note that the first four methods of this sequence are the same as the first four methods in the previous property-setting sequences.)

|     | Method                                             | Invoked by                                                         | Purpose                                                                                           |
|-----|----------------------------------------------------|--------------------------------------------------------------------|---------------------------------------------------------------------------------------------------|
| 1   | **CMyDevice::OnPrepareHardware**                   | WUDFx.dll (a component of the Windows user-mode driver framework). | Starts the operations required to make the given device accessible by the driver.                 |
| 2   | **CSensorDdi::Initialize**                         | **CMyDevice::OnPrepareHardware**                                   | Create and initialize the sensor device object.                                                   |
| 3   | **CSensorDevice::Initialize**                      | **CSensorDdi::Initialize**                                         | Initializes the sensor driver interface, the client manager, and the report manager.              |
| 4   | **CSensorDevice::InitializeSensorDriverInterface** | **CSensorDevice::Initialize**                                      | Starts the initialization of the objects that store the property keys and datafield values.       |
| 5   | **CAccelerometerDevice::SetDefaultPropertyValues** | **CSensorDevice::InitializeSensorDriverInterface**                 | Sets the default property values for the accelerometer (manufacturer, model, serial number, etc.) |

 

### Retrieving the default writeable properties

| Module                  | Class/Interface      |
|-------------------------|----------------------|
| Device.cpp              | CMyDevice            |
| SensorDdi.cpp           | CSensorDdi           |
| AccelerometerDevice.cpp | CAccelerometerDevice |
| SensorDevice.cpp        | CSensorDevice        |

 

The Windows sensor platform supports read-only and read-write properties for sensors and this is true of the default properties as well. The code in the SpbAccelerometer sample gets the list of writeable (or settable) default properties as part of the driver and device initialization phase. The methods below are invoked by the driver, during initialization, to get these properties for the accelerometer. (Note that the first four methods of this sequence are the same as the first four methods in the previous property-setting sequences.)

|     | Method                                             | Invoked by                                                         | Purpose                                                                                           |
|-----|----------------------------------------------------|--------------------------------------------------------------------|---------------------------------------------------------------------------------------------------|
| 1   | **CMyDevice::OnPrepareHardware**                   | WUDFx.dll (a component of the Windows user-mode driver framework). | Start the operations required to make the given device accessible by the driver.                  |
| 2   | **CSensorDdi::Initialize**                         | **CMyDevice::OnPrepareHardware**                                   | Creates and initialize the sensor device object.                                                  |
| 3   | **CSensorDevice::Initialize**                      | **CSensorDdi::Initialize**                                         | Initializes the sensor driver interface, the client manager, and the report manager.              |
| 4   | **CSensorDevice::InitializeSensorDriverInterface** | **CSensorDevice::Initialize**                                      | Starts the initialization of the objects that store the property keys and datafield values.       |
| 5   | **CAccelerometerDevice::SetDefaultPropertyValues** | **CSensorDevice::InitializeSensorDriverInterface**                 | Sets the default property values for the accelerometer (manufacturer, model, serial number, etc.) |

 

### Activating support for events

| Module                  | Class/Interface      |
|-------------------------|----------------------|
| Device.cpp              | CMyDevice            |
| SensorDdi.cpp           | CSensorDdi           |
| AccelerometerDevice.cpp | CAccelerometerDevice |
| SensorDevice.cpp        | CSensorDevice        |

 

The Windows sensor platform supports events. An application registers an event handler to get notifications from the driver. For an accelerometer, these notifications are triggered when a certain change sensitivity (measured in G force) is exceeded or the current report interval expires.

To support the event model in the sensor platform, the driver must activate a thread to handle the event notifications. The methods below are invoked by the driver during initialization to perform this activation. (Note that the first three methods of this sequence are the same as the first three methods in a number of the previous sequences.)

|     | Method                                         | Invoked by                                                         | Purpose                                                                              |
|-----|------------------------------------------------|--------------------------------------------------------------------|--------------------------------------------------------------------------------------|
| 1   | **CMyDevice::OnPrepareHardware**               | WUDFx.dll (a component of the Windows user-mode driver framework). | Starts the operations required to make the given device accessible by the driver.    |
| 2   | **CSensorDdi::Initialize**                     | **CMyDevice::OnPrepareHardware**                                   | Creates and initializes the sensor device object.                                    |
| 3   | **CSensorDevice::Initialize**                  | **CSensorDdi::Initialize**                                         | Initializes the sensor driver interface, the client manager, and the report manager. |
| 4   | **CReportManager::Initialize**                 | **CSensorDevice::Initialize**                                      | Creates the thread used to handle events.                                            |
| 5   | **CReportManager::ActivateDataEventingThread** | **CReportManager::Initialize**                                     | Activates the thread created by the previous method.                                 |

 

### Initializing the class extension

| Module     | Class/Interface |
|------------|-----------------|
| Device.cpp | CMyDevice       |

 

The Windows sensor platform has a class extension of the Sensor API that provides a standard mechanism for getting sensor data and raising event notifications. The sample driver invokes the **ISensorClassExtension::Initialize** method to initialize the class extension after it receives the call to **CMyDevice::OnPrepareHardware**.

### Configuring the device and placing it in standby mode

| Module                  | Class/Interface      |
|-------------------------|----------------------|
| Device.cpp              | CMyDevice            |
| SensorDdi.cpp           | CSensorDdi           |
| AccelerometerDevice.cpp | CAccelerometerDevice |
| SensorDevice.cpp        | CSensorDevice        |

 

The final sequence of methods in the device and driver initialization configures the ADXL345 and places it in standby mode. (This sequence of write and read operations is repeated multiple times until the device is configured.)

|     | Method                                          | Invoked by                                                         | Purpose                                                                               |
|-----|-------------------------------------------------|--------------------------------------------------------------------|---------------------------------------------------------------------------------------|
| 1   | **CMyDevice::OnD0Entry**                        | WUDFx.dll (a component of the Windows user-mode driver framework). | Invoked when a new device appears on the system.                                      |
| 2   | **CSensorDdi::Start**                           | **CMyDevice::OnD0Entry**                                           | A pass-through method that calls CSensorDevice::Start.                                |
| 3   | **CSensorDevice::Start**                        | **CSensorDdi::Start**                                              | Initiates the device configuration process.                                           |
| 4   | **CAccelerometerDevice::ConfigureHardware**     | **CSensorDevice::Start**                                           | Initiates the operation that writes a value to the specified register of the ADXL345. |
| 5   | **CAcclerometerDevice::WriteRegister**          | **CAccelerometerDevice::ConfigureHardware**                        | Initiates the operation that writes a value to the specified register of the ADXL345. |
| 6   | **CSpbRequest::CreateAndSendWrite**             | **CAcclerometerDevice::WriteRegister**                             | Transmits the write request over the I2C bus                                          |
| 7   | **CAcclerometerDevice::ReadRegister**           | **CAccelerometerDevice::ConfigureHardware**                        | Initiates the operation that reads a value from the specified ADXL345 register.       |
| 8   | **CSpbRequest::CreateAndSendWriteReadSequence** | **CAcclerometerDevice::ReadRegister**                              | Receives the read results over the I2C bus.                                           |
| 9   | **CSpbRequest::CreateAndSendIoctl**             | **CSpbRequest::CreateAndSendWriteReadSequence**                    | Helper method that creates and sends an IOCTL request.                                |

 

Most of the device-configuration work takes place through a series of **CAccelerometerDevice::WriteRegister** and **CAccelerometerDevice::ReadRegister** method calls. The driver uses the ::**WriteRegister** method to write a value to one of the ADXL345 registers; it then examines the value returned in the corresponding ::**ReadRegister** method to verify that the write operation succeeded. Here's a complete sequence of write and read operations.

|     | Method                                  | Register | Data                | Purpose                                                                                                            |
|-----|-----------------------------------------|----------|---------------------|--------------------------------------------------------------------------------------------------------------------|
| 1   | **CAccelerometerDevice::WriteRegister** | **0x2d** | **'\\0' (0x00)**    | Resets the sensor’s power-control register and place the device in standby mode.                                   |
| 2   | **CAccelerometerDevice::ReadRegister**  | **0x2d** | **'\\0' (0x00)**    | The returned register values indicate that the write operation succeeded.                                          |
| 3   | **CAccelerometerDevice::WriteRegister** | **0x31** | **'\\v' (0x0b)**    | Sets the device in full-resolution mode with a range along each axis of +/- 16G.                                   |
| 4   | **CAccelerometerDevice::ReadRegister**  | **0x31** | **'\\v' (0x0b**     | The returned register values indicate that the write operation succeeded.                                          |
| 5   | **CAccelerometerDevice::WriteRegister** | **0x38** | **'\\0' (0x00)**    | Resets the sensor’s FIFO control register to the bypass mode.                                                      |
| 6   | **CAccelerometerDevice::ReadRegister**  | **0x38** | **'\\0' (0x00)**    | The returned register values indicate that the write operation succeeded.                                          |
| 7   | **CAccelerometerDevice::WriteRegister** | **0x2C** | **'\\a' (0x07)**    | Sets the BW\_RATE register to initiate low-power mode.                                                             |
| 8   | **CAccelerometerDevice::ReadRegister**  | **0x2C** | **'\\a' (0x07)**    | The returned register values indicate that the write operation succeeded.                                          |
| 9   | **CAccelerometerDevice::WriteRegister** | **0x24** | **'\\x1' (0x01)**   | Sets the TRESH\_ACT (activity threshold) register to 1.                                                            |
| 10  | **CAccelerometerDevice::ReadRegister**  | **0x24** | **'\\x1' (0x01)**   |                                                                                                                    |
| 11  | **CAccelerometerDevice::WriteRegister** | **0x27** | **(0xf0)**          | Sets the ACT\_INACT\_CTL (active/inactive) register to 0xf0.                                                       |
| 12  | **CAccelerometerDevice::ReadRegister**  | **0x27** | **(0xf0)**          | The returned register value indicates that write operation succeeded.                                              |
| 13  | **CAccelerometerDevice::WriteRegister** | **0x2f** | **'\\0x10' (0x10)** | Sets the INT\_MAP (interrupt mapping) register. A value of 0x10 requests that the Watermark is mapped to INT2 pin. |
| 14  | **CAccelerometerDevice::ReadRegister**  | **0x2f** | **'\\0x10' (0x10)** | The returned register value indicates that the write operation succeeded.                                          |

 

After the driver and device have been configured, the initialization sequence is complete and apps can start receiving sensor data.

 

 




