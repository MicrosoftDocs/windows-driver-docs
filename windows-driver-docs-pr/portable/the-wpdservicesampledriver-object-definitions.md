---
Description: Defining the Service Objects
MS-HAID: 'wpddk.the\_wpdservicesampledriver\_object\_definitions'
MSHAttr: 'PreferredLib:/library/windows/hardware'
title: Defining the Service Objects
---

# Defining the Service Objects


In WPD, the logical entities on devices are referred to as objects. Objects can represent informational or functional parts of a device. Any object has one or more properties. You can think of the properties as object-description metadata. For example, the Contacts service object on the sample driver supports a Name property that specifies a friendly-name for the service.

The WpdHelloWorldDriver supports the objects that are shown in the following table.

| Object  | Description                                                                                                       |
|---------|-------------------------------------------------------------------------------------------------------------------|
| Device  | The root object that contains descriptive properties like the firmware version, the model, and the friendly name. |
| Storage | An object that exposes properties like a storage capacity, a file-system type, and a count of free bytes.         |
| Folder  | An object that exposes properties like a folder name.                                                             |
| File    | An object that exposes properties like a file name and actual file contents.                                      |

 

Similar to the WpdHelloWorldDriver, the WpdServiceSampleDriver continues to support a Storage object. However, because the sample does not support a folder or file (for simplicity), we removed these objects and replaced them with a single object that corresponds to a Contact. The following table lists the objects that the new driver supports.

| Object   | Description                                                                                                            |
|----------|------------------------------------------------------------------------------------------------------------------------|
| Device   | The root object that contains descriptive properties like the firmware version, the model, and the friendly name.      |
| Storage  | An object that exposes properties like a storage capacity, a file-system type, and a count of free bytes.              |
| Contacts | A service object that contains properties like an object identifier, a persistent unique ID (PUID), a name, and so on. |

 

In WPD, objects are identified by strings. The string identifier for the Device Object is defined in the *Portabledevice.h* header file:

```
#define WPD_DEVICE_OBJECT_ID  L"DEVICE"
```

The string identifiers for the Storage object are defined in the *FakeStorage.h* header file:

```
#define STORAGE_OBJECT_ID                                 L"123ABC"
#define STORAGE_CAPACITY_VALUE                            1024 * 1024
#define STORAGE_FREE_SPACE_IN_BYTES_VALUE                 STORAGE_CAPACITY_VALUE
#define STORAGE_SERIAL_NUMBER_VALUE                       L"98765432109876-54321098765432"
#define STORAGE_OBJECT_NAME_VALUE                         L"Internal Memory"
#define STORAGE_FILE_SYSTEM_TYPE_VALUE                    L"FAT32"
#define STORAGE_DESCRIPTION_VALUE                         L"Phone Memory Storage System"
#define STORAGE_CONTAINER_FUNCTIONAL_OBJECT_ID            WPD_DEVICE_OBJECT_ID
#define STORAGE_TYPE                                      WPD_STORAGE_TYPE_FIXED_ROM
```

The string identifiers for the Contacts object are defined in the *FakeContactsServiceContent.h* header file:

```
#define CONTACTS_SERVICE_OBJECT_ID                        L"789DEF"
#define CONTACTS_SERVICE_PERSISTENT_UNIQUE_ID             L"{95A95EA9-9904-430E-8FF6-70851F208478}"
#define CONTACTS_SERVICE_OBJECT_NAME_VALUE                L"Contacts"
#define CONTACTS_SERVICE_HUMAN_READABLE_NAME              L"Hello World Phone Contacts"
#define CONTACTS_SERVICE_PREFERRED_FORMAT                 WPD_OBJECT_FORMAT_ABSTRACT_CONTACT
#define CONTACTS_SERVICE_VERSION                          L"1.0"

#define NUM_CONTACT_OBJECTS                               10
```

These object identifier constants are passed to a method in a source module that handles functional-object retrieval (*FakeDevice.cpp*) . The following excerpt from the **FakeDevice::GetFunctionalObjects** method shows how to use the CONTACTS\_SERVICE\_OBJECT\_ID to build a collection of supported functional objects (SERVICE\_Contacts is defined in the *ContactsDeviceService.h* header file and represents the functional category of the service object):

```
    // Add CONTACTS_SERVICE_OBJECT_ID to the functional object identifiers collection
    if (hr == S_OK)
    {
        if ((guidFunctionalCategory  == SERVICE_Contacts) ||
            (guidFunctionalCategory  == WPD_FUNCTIONAL_CATEGORY_ALL))
        {
            pv.vt       = VT_LPWSTR;
            pv.pwszVal  = CONTACTS_SERVICE_OBJECT_ID;
            hr = pFunctionalObjects->Add(&pv);
            CHECK_HR(hr, "Failed to add contacts service object ID");
        }
    }
```

## <span id="related_topics"></span>Related topics


****
[The WpdServiceSampleDriver Sample](the-wpdservicesampledriver-sample.md)

[The WPD Driver Samples](the-wpd-driver-samples.md)

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[wpd_dk\wpddk]:%20Defining%20the%20Service%20Objects%20%20RELEASE:%20%281/5/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




