---
title: Troubleshooting Specific WMI Problems
description: Troubleshooting Specific WMI Problems
ms.assetid: 966191e7-aec4-4eff-b975-99a6d3eb8d02
keywords: ["WMI WDK kernel , troubleshooting", "troubleshooting WMI problems WDK"]
ms.date: 06/16/2017
ms.localizationpriority: medium
---

# Troubleshooting Specific WMI Problems





### <a href="" id="driver-s-wmi-classes-do-not-appear-in-the--root-wmi-namespace"></a>Driver's WMI Classes Do Not Appear in the \\root\\wmi Namespace

1.  Use [wmimofck](using-wmimofck-exe.md)driver.bmf to check if the binary MOF file format is correct. Additional error messages may be found in mofcomp.log.

2.  Check the [system event log](general-techniques-for-testing-wmi-driver-support.md#ddk-wmi-irps-and-the-system-event-log-kg) to see if the driver is returning a malformed [**WMIREGINFO**](https://msdn.microsoft.com/library/windows/hardware/ff565832) data structure in response to the registration request.

3.  Check that the driver is returning the correct values for **RegistryPath** and **MofResourceName** within the **WMIREGINFO** structure.

4.  If the driver provides its MOF data in a separate file, check that the [MofImagePath](setting-the-mofimagepath-registry-value.md) registry value for the driver is set correctly.

5.  Check the [WMI WDM provider log](general-techniques-for-testing-wmi-driver-support.md#ddk-wmi-wdm-provider-log-kg) for errors.

6.  Use [Mofcomp](compiling-a-driver-s-mof-file.md) to recompile and reload your MOF text file. For example, the command **mofcomp -N:root/wmi driver.mof** will try to recompile and reload any MOF data in the driver.mof file. Check to see what error messages Mofcomp generates in mofcomp.log. (Note that if your MOF file uses preprocessor directives such as **\#define**, you will need to use the already-preprocessed MOF file, and not the original source file.

    **Warning**  If this operation succeeds, it actually registers the new WMI class data with the system. You will need to delete these classes (by using Wbemtest, for example) to test if your driver's MOF data is being read correctly.

     

7.  If the previous step succeeds, then the most likely problem is that the members of **WMIREGINFO**, such as **MofResourceName**, are specified incorrectly. Alternatively, the problem could be that your MOF file specifies a class derived from a base class that does not exist.

8.  If the driver is using dynamic MOF data (see [Implementing Dynamic MOF Data](implementing-dynamic-mof-data.md)), check that the driver is receiving WMI IRP requests for the MSWmi\_MofData\_GUID GUID and that it is completing the IRP successfully and with no error logged.

### Driver's WMI Properties or Methods Cannot Be Accessed

1. Use **wmimofck driver.bmf** to check if the binary MOF file format is correct. For more information, see [Using wmimofck.exe](using-wmimofck-exe.md).

2. Check the system event log for errors. For more information, see [WMI IRPs and the System Event Log](general-techniques-for-testing-wmi-driver-support.md#ddk-wmi-irps-and-the-system-event-log-kg).

3. Check the [WMI WDM Provider Log](general-techniques-for-testing-wmi-driver-support.md#ddk-wmi-wdm-provider-log-kg) for errors.

4. Make sure the driver receives a WMI IRP whenever you use Wbemtest to query the driver's classes. If not, then check that the specified GUID in the MOF file matches the GUID the driver is expecting. Also check that the driver is receiving the WMI registration request, that it is succeeding, and the driver is registering the right GUIDs.

5. If the driver receives the IRP, ensure that the IRP is completed successfully, and that the driver is returning the right type of **WNODE\_*XXX*** structure.

6. If Wbemtest returns an error, click the **More Information** button and check the **Description** property for a description of the error.

7. For methods, check that your driver supports handling the [**IRP\_MN\_QUERY\_ALL\_DATA**](https://msdn.microsoft.com/library/windows/hardware/ff551650) and [**IRP\_MN\_QUERY\_SINGLE\_INSTANCE**](https://msdn.microsoft.com/library/windows/hardware/ff551718) requests for the method's GUID. WMI will always perform one of those two requests before executing a method.

### Driver's WMI Events Are Not Being Received

1.  Check the [system event log](general-techniques-for-testing-wmi-driver-support.md#ddk-wmi-irps-and-the-system-event-log-kg) for errors. For example, if the driver specifies a static event name when calling [**IoWMIWriteEvent**](https://msdn.microsoft.com/library/windows/hardware/ff550520) but the driver did not register any static event names, this would produce an entry in the system event log.

2.  Check the [WMI WDM provider log](general-techniques-for-testing-wmi-driver-support.md#ddk-wmi-wdm-provider-log-kg) for errors.

3.  If the driver is sending an event reference, the driver should receive an [**IRP\_MN\_QUERY\_SINGLE\_INSTANCE**](https://msdn.microsoft.com/library/windows/hardware/ff551718) request immediately after sending the event reference. If the driver does not receive the IRP, the [**WNODE\_EVENT\_REFERENCE**](https://msdn.microsoft.com/library/windows/hardware/ff566374) structure may have been malformed. If the driver receives the IRP, it should be completing it with status STATUS\_SUCCESS.

4.  If the driver uses [**IoWMIWriteEvent**](https://msdn.microsoft.com/library/windows/hardware/ff550520) to send the event or event reference, make sure the event structure (either [**WNODE\_SINGLE\_INSTANCE**](https://msdn.microsoft.com/library/windows/hardware/ff566377) or **WNODE\_EVENT\_REFERENCE**) is filled out correctly. In particular, if the event GUID is registered for static instance names, make sure that the correct instance index and provider ID are provided. If the event GUID is registered for dynamic instance names, make sure the instance name is included when the event is sent. If using the **WNODE\_EVENT\_REFERENCE** structure to specify the event, check that **Wnode.Guid** matches **TargetGuid**.

5.  If the driver uses [**WmiFireEvent**](https://msdn.microsoft.com/library/windows/hardware/ff565807) to send the event, make sure the correct value is passed for the *Guid* and *InstanceIndex* parameters.

### Changes in Security Settings for WMI Requests Do Not Take Effect

-   Unload and reload the WMI WDM Provider. For WMI data blocks registered with the WMIREG\_FLAG\_EXPENSIVE flag, the provider keeps a handle open to the data block as long as there are consumers for that block. The new security settings will not take effect until the provider closes the handle. Unloading and reloading the provider makes sure the handle has been closed. (For more information about the WMIREG\_FLAG\_EXPENSIVE flag, see [**WMIREGGUID**](https://msdn.microsoft.com/library/windows/hardware/ff565827).)

 

 




