---
title: Device Support
description: Device Support
ms.assetid: 41316BB1-0AE0-4100-AE7B-0014FE9FD0E7
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Device Support


If your test automation relies on presence of devices or test resources, refer to the example, TestResourceExample, and follow along on how to leverage the device-support or test resource support available in TAEF. Please make sure that you are familiar with how to author basic tests using TAEF and the basic execution of TAEF before proceeding.

## <span id="Authoring_for_device_support_-_Sources_file"></span><span id="authoring_for_device_support_-_sources_file"></span><span id="AUTHORING_FOR_DEVICE_SUPPORT_-_SOURCES_FILE"></span>Authoring for device support - Sources file


Te.Common.lib is required in addition to other libraries needed author a test in TAEF.

## <span id="Authoring_for_device_support_-_Test_Resource_definition"></span><span id="authoring_for_device_support_-_test_resource_definition"></span><span id="AUTHORING_FOR_DEVICE_SUPPORT_-_TEST_RESOURCE_DEFINITION"></span>Authoring for device support - Test Resource definition


Users are responsible for creating their own Test Resource (device) definition. To do this, you need to implement ITestResource. ITestResource is defined in the published header file ITestResource.h and looks as follows:

```cpp
namespace WEX { namespace TestExecution
{
    namespace TestResourceProperty
    {
        // the following are reserved and must have properties for any TestResource definition
        static const wchar_t c_szName[] = L"Name";
        static const wchar_t c_szId[] = L"Id";
        static const wchar_t c_szGuid[] = L"GUID";
        static const wchar_t c_szType[] = L"Type";
    }

    struct __declspec(novtable) __declspec(uuid("79098e4c-b78d-434b-854d-2b59f5c4acc5")) ITestResource : public IUnknown
    {
    public:
        virtual HRESULT STDMETHODCALLTYPE GetGuid(GUID* pGuid) = 0;
        virtual HRESULT STDMETHODCALLTYPE SetGuid(GUID guid) = 0;
        virtual HRESULT STDMETHODCALLTYPE GetValue(BSTR name, BSTR* pValue) = 0;
        virtual HRESULT STDMETHODCALLTYPE SetValue(BSTR name, BSTR value) = 0;
    };
} /*namespace TestExecution*/ } /*namespace WEX*/
```

In our example, class MyTestResource implements ITestResource COM Interface. In ITestResource.h, you will also find a list of "must-have" properties defined. It should be possible to obtain the GUID for the test resource using GetGuid(..) and the Name, Id and Type of the resource using GetValue(...). If any of this are missing in a TestResource, TAEF will consisder it to be invalid and not maintain it's information.(See "Building the resource list" section that follows).

## <span id="Authoring_for_device_support_-_Specifying_resource_dependent_metadata"></span><span id="authoring_for_device_support_-_specifying_resource_dependent_metadata"></span><span id="AUTHORING_FOR_DEVICE_SUPPORT_-_SPECIFYING_RESOURCE_DEPENDENT_METADATA"></span>Authoring for device support - Specifying resource dependent metadata


In order to specify that the test module has test resource dependent test methods, a module level metadata property **'TestResourceDependent"** must be set to "true". The property gets inherited by all the classes in the test module and by all the test methods in these classes. If any of the test method in the module is not test resource dependent, then it should explicitly re-set the metadata value to false. All of the other test methods that depend on test resource must provide a selection query using the test resource's "Id" and/or "Type".

Here are some quick sample "ResourceSelection" for our example resource list and what each of them implies:

-   "@Id='HD\*'": matches each resource with an Id starting with "HD"
-   "@Type='PCI'": matches each resource of Type "PCI"
-   "@Id='PCI\*' OR @Id='HD\*'": matches each resource starting with "PCI" or starting with "HD"
-   "@Type='PCI' and @id='\*37'": matches each resource one of type "PCI" with a name ending in "37"

In our example code, this looks as follows:

```cpp
BEGIN_MODULE()
    MODULE_PROPERTY(L"TestResourceDependent", L"true")
END_MODULE()

    class TestResourceExample
    {
        TEST_CLASS(TestResourceExample);

        BEGIN_TEST_METHOD(NoTestResourceTest)
            TEST_METHOD_PROPERTY(L"TestResourceDependent", L"false")
        END_TEST_METHOD()

        BEGIN_TEST_METHOD(OneHDAudioTest)
            TEST_METHOD_PROPERTY(L"ResourceSelection", L"@Id=&#39;HD*&#39;")
        END_TEST_METHOD()

        ...

        BEGIN_TEST_METHOD(HDorPCITest)
            TEST_METHOD_PROPERTY(L"ResourceSelection", L"@Id=&#39;PCI*&#39; OR @Id=&#39;HD*&#39;")
        END_TEST_METHOD()
        ...
    };
```

In the example above, you will see that the module is marked as "TestResourceDependent". The NoTestResourceTest is explicitly marked as not dependent on any test resource by setting "TestRssourceDependent" metadata to "false". All other test methods specify a selection criteria for the test resources they are interested in executing for.

The Selection criteria grammar is very similar to the commandline selection query grammar available for TAEF. In the case of resource selection however, it is restricted to the use of resource Id's and types. Since resource Id is a String, it needs to be enclosed in single quotes. You can use the wildcard characters "\*" or "?" in the specification of the Id value. In our example above, in OneHDAudioTest, the resource selection specifies a match to any resource where Id starts with 'HD'. Similarly, in the case of HDorPCITest, the resource selection will match any resource where Id starts with 'HD' or starts with 'PCI'. It's important to note that the resource selection is case insensitive - that is, 'pci', 'Pci' and 'PCI' will all be treated the same.

Based on the resource selection, TAEF will re-invoke the test method along with the test level setup and cleanup methods (if they are specified) once for each test resource that matches the selection. The following sections will examine the details on how to specify the list of resources and provide it to TAEF and how the test method can retrieve the resources in the next section.

## <span id="Authoring_for_device_support_-_Building_the_resource_list"></span><span id="authoring_for_device_support_-_building_the_resource_list"></span><span id="AUTHORING_FOR_DEVICE_SUPPORT_-_BUILDING_THE_RESOURCE_LIST"></span>Authoring for device support - Building the resource list


As soon as TAEF encounters a TestResourceDependent test module, it will look for and invoke the dll-exported method BuildResourceList. It is in the implementation of BuildResourceList where users can create new test resources and add them to the interface that gets passed in as a parameter to BuildResourceList. Let's take a look at the implementation of this method in our example:

```cpp
using namespace WEX::TestExecution;
HRESULT __cdecl BuildResourceList(ResourceList& resourceList)
{
    Log::Comment(L"In BuildResourceList");

    GUID myGuid;
    VERIFY_SUCCEEDED(::CoCreateGuid(&myGuid));

    CComPtr<ITestResource> spTestResource;
    spTestResource.Attach(new MyTestResource(L"HDAudio1", L"HDAudio-deviceid-1", myGuid, L"HD"));
    resourceList.Add(spTestResource);

    spTestResource.Attach(new MyTestResource(L"HDAudio2", L"HDAudio-deviceid-2", myGuid, L"HD"));
    resourceList.Add(spTestResource);

    spTestResource.Attach(new MyTestResource(L"PCI1", L"PCI-deviceid-1", myGuid, L"PCI"));
    resourceList.Add(spTestResource);

    spTestResource.Attach(new MyTestResource(L"PCI2", L"PCI-deviceid-2", myGuid, L"PCI"));
    resourceList.Add(spTestResource);

    spTestResource.Attach(new MyTestResource(L"PCI3", L"PCI-deviceid-3", myGuid, L"PCI"));
    resourceList.Add(spTestResource);

    return S_OK;
}
```

BuildResourceList accepts a reference to WEX::TestExecution::ResourceList as its parameter. ResourceList is defined in the published header file ResourceList.h. Using the Add(...) method on the ResourceList, users can add all the test resources discovered or created for TAEF to manage and work with. The example above added 5 such test resources.

The Add method will fail if the test resource to be added fails to return either the "Name", "Id", "Type" or GUID for the resource.

The ResourceList will be maintained through the lifetime of the test module - that is, until all the test methods and cleanup methods are done executing. If BuildResourceList returns a FAILED HRESULT value, all resource dependent test methods in the test module are logged as blocked without executing. All non test resource will get executed regardless.

BuildResourceList is invoked before any other methods in the test module. After the resource list is built (in BuildResourceList), the "ResourceSelection" metadata is used to match available resources in the resource list. If a match is found, all setup methods (module, class, test order) are invoked followed by the test method itself. The test level cleanup method is called after each test invocation.

Behind the scenes, TAEF retains the ResourceList on which the resource selection is applied. For example, for OneHDAudioTest test method, the test resources with Ids "HDAudio-deviceid-1" and "HDAudio-deviceid-2" will both match 'HD\*' and for each of these, the test method will get re-invoked by TAEF (once for each). There will also be an implicit index associated with each invocation of the test. So you will see &lt;namespace qualifier&gt;OneHDAudioTest\#0 and &lt;namespace qualifier&gt;OneHDAudioTest\#1 as the two invocations.

## <span id="Authoring_for_device_support_-_Retrieving_the_device_in_a_test_method"></span><span id="authoring_for_device_support_-_retrieving_the_device_in_a_test_method"></span><span id="AUTHORING_FOR_DEVICE_SUPPORT_-_RETRIEVING_THE_DEVICE_IN_A_TEST_METHOD"></span>Authoring for device support - Retrieving the device in a test method


Previous sections looked at how to add the necessary metadata at module, class and test method level. They also looked at how to define custom test resources and how to add them to the ResourceList in the implementation of BuildResourceList. The next part that follows is retrieving the resources in the test method. Let's take a look at one of the simple test methods in our example:

```cpp
1   void TestResourceExample::OneHDAudioTest()
2   {
3       Log::Comment(L"In HD audio test");
4       size_t count = Resources::Count();
5       size_t index = 0;
6       VERIFY_ARE_EQUAL(count, (index + 1));
7
8       CComPtr<ITestResource> spTestResource;
9       VERIFY_SUCCEEDED(Resources::Item(index, &spTestResource));
10
11      // Get Resource Id
12      CComBSTR value;
13      VERIFY_SUCCEEDED(spTestResource->GetValue(CComBSTR(TestResourceProperty::c_szId), &value));
14      Log::Comment(L"Resource Id is " + String(value));
15  }
```

In OneHDAudioTest, the resource selection selects one test resource at a time where the resource Id starts with 'HD'. The static class Resources defined in ResourceList.h provides the APIs for retrieving the count as well as the actual resource available during any given invocation of the test. In this case, as you can see in lines 4, 9, and 13 in the example above, Resources::Count() gives the count of number of test resources available during the current invocation of the test method. In this test method, this should be 1. You can verify this value by using the VERIFY macros that are available in TAEF (Verify.h). As you know, if any of the verify calls fails in an exception based TAEF test, the execution will terminate at that point and the test method would be marked as Failed.

Next, using Resources::Item(...) API and passing in an index at which to retrieve the resource (in this case since only one test resource will be available during an invocation, index will always be 0), you can retrieve the test resource. The test method can further use the retrieved test resource as it needs for its testing.

The same basic principle is followed in all test methods. Take a look at other test methods in the example to get a better understanding.

## <span id="Executing_a_test_resource_dependent_test_module"></span><span id="executing_a_test_resource_dependent_test_module"></span><span id="EXECUTING_A_TEST_RESOURCE_DEPENDENT_TEST_MODULE"></span>Executing a test resource dependent test module


With the test resource dependent tests now authored and built, you can now execute it using TAEF. The key point to note is that TestResourceDependent tests can only be executed inproc. This means that even if you don't explicitly specify **"/inproc"** switch, it will get added on as soon as TAEF discovers the test resource dependent test module. As you may know, tests from only one test module can be executed in a given TAEF execution when the "/inproc" switch is present. This means you can not specify more than one test module at the commandline if your test module is resource dependent.

To actually execute all the tests in our test module, you can simply run:

``` syntax
te Examples\Cpp.TestResource.Example.dll
```

A useful way to just get a listing of all the test method invocations and the data and metadata combinations without actually running the test methods, is to use **/listproperties** switch at the commandline. Let's take a look at the output.

``` syntax
te Examples\Cpp.TestResource.Example.dll /listproperties

Test Authoring and Execution Framework v2.9.3k for x86
In BuildResourceList
Verify: SUCCEEDED(::CoCreateGuid(&myGuid))

        f:\toolsdev.binaries.x86chk\WexTest\CuE\TestExecution\Examples\Cpp.TestResource.Example.dll
                Property[TestResourceDependent] = true

            WEX::TestExecution::Examples::TestResourceExample
                WEX::TestExecution::Examples::TestResourceExample::NoTestResourceTest
                        Property[TestResourceDependent] = false

                WEX::TestExecution::Examples::TestResourceExample::OneHDAudioTest#0
                        Property[ResourceSelection] = @Id='HD*' 
                
                            Resource#0
                                Id = HDAudio-deviceid-1
                                Name = HDAudio1
                                Type = HD

                WEX::TestExecution::Examples::TestResourceExample::OneHDAudioTest#1
                        Property[ResourceSelection] = @Id='HD*'
                        
                            Resource#0
                                Id = HDAudio-deviceid-2
                                Name = HDAudio2
                                Type = HD

                WEX::TestExecution::Examples::TestResourceExample::OnePCIDeviceTest#0
                        Property[ResourceSelection] = @Id='PCI*'
                        
                            Resource#0
                                Id = PCI-deviceid-1
                                Name = PCI1
                                Type = PCI

                WEX::TestExecution::Examples::TestResourceExample::OnePCIDeviceTest#1
                        Property[ResourceSelection] = @Id='PCI*'
                        
                            Resource#0
                                Id = PCI-deviceid-2
                                Name = PCI2
                                Type = PCI

                WEX::TestExecution::Examples::TestResourceExample::OnePCIDeviceTest#2
                         Property[ResourceSelection] = @Id='PCI*'
                        
                            Resource#0
                                Id = PCI-deviceid-3
                                Name = PCI3
                                Type = PCI

                WEX::TestExecution::Examples::TestResourceExample::HDorPCITest#0
                        Property[ResourceSelection] = @Id='PCI*' OR @Id='HD*'
                        
                            Resource#0
                                Id = HDAudio-deviceid-1
                                Name = HDAudio1
                                Type = HD

                WEX::TestExecution::Examples::TestResourceExample::HDorPCITest#1
                         Property[ResourceSelection] = @Id='PCI*' OR @Id='HD*'
                        
                            Resource#0
                                Id = HDAudio-deviceid-2
                                Name = HDAudio2
                                Type = HD

                WEX::TestExecution::Examples::TestResourceExample::HDorPCITest#2
                         Property[ResourceSelection] = @Id='PCI*' OR @Id='HD*'
                        
                            Resource#0
                                Id = PCI-deviceid-1
                                Name = PCI1
                                Type = PCI

                WEX::TestExecution::Examples::TestResourceExample::HDorPCITest#3
                         Property[ResourceSelection] = @Id='PCI*' OR @Id='HD*'
                        
                            Resource#0
                                Id = PCI-deviceid-2
                                Name = PCI2
                                Type = PCI

                WEX::TestExecution::Examples::TestResourceExample::HDorPCITest#4
                         Property[ResourceSelection] = @Id='PCI*' OR @Id='HD*'
                        
                            Resource#0
                                Id = PCI-deviceid-3
                                Name = PCI3
                                Type = PCI

                WEX::TestExecution::Examples::TestResourceExample::PCI1AudioTest #0
                         Property[ResourceSelection] = @Id='PCI*' AND @Id='*1'
                        
                            Resource#0
                                Id = PCI-deviceid-1
                                Name = PCI1
                                Type = PCI
```

Notice the implicit index that gets added to the test method name during each invocation of a test resource depent test method. The ResourceSelection property is shown followed by a list of all the resources that will be available to the test method in the order they will be available. For example, in case of the third invocation of HDAudioHDAudioPCITest (HDAudioHDAudioPCITest\#2), HDAudio-deviceid-1 will be the resource available at index 0 in Resources::Item(...).

You can be more specific about which test invocation you are interested in by using the commandline selection query language available in TAEF. For example to select all invocations of test methods where the test resources 'PCI-deviceid-3' is available, you can use the selection criteria:

``` syntax
te Examples\Cpp.TestResource.Example.dll /list
          /select:"@Resource:Id='PCI-deviceid-3'"

Test Authoring and Execution Framework v2.9.3k for x86
In BuildResourceList
Verify: SUCCEEDED(::CoCreateGuid(&myGuid))

        f: \Examples\Cpp.TestResource.Example.dll
            WEX::TestExecution::Examples::TestResourceExample
                WEX::TestExecution::Examples::TestResourceExample::OnePCIDeviceTest#2
                WEX::TestExecution::Examples::TestResourceExample::HDorPCITest#4
```

Similarly, to select a particular test method by name (note test method names are fully qualified along with the invocation index appended in the end), you can use a selection query as follows:

``` syntax
te Examples\Cpp.TestResource.Example.dll /name:*OneHDAudioTest#1
Test Authoring and Execution Framework v2.2 Build 6.1.7689.0 (release.091218-1251) for x86

Discovered a test resource dependent test module. Assuming /InProc execution.

In BuildResourceList
Verify: SUCCEEDED(::CoCreateGuid(&myGuid))

StartGroup: WEX::TestExecution::Examples::TestResourceExample::OneHDAudioTest#1
In HD audio test
Verify: AreEqual(count, (index + 1))
Verify: SUCCEEDED(Resources::Item(index, &spTestResource))
Verify: SUCCEEDED(spTestResource->GetValue(CComBSTR(TestResourceProperty::c_szId), &value))
Resource Id is HDAudio-deviceid-2
WEX::TestExecution::Examples::TestResourceExample::OneHDAudioTest#1 [Passed]

Summary: Total=1, Passed=1, Failed=0, Blocked=0, Not Run=0, Skipped=0
```

Note the implicit inproc added warning in the third line of the example above. The above selection query had the same effect as selection query:**/select:"@Name='\*OneHDAudio\*' And @Resource:Index=1"**. It is also possible to select a resource using its Name or Type (or Id as shown above). For example, **/select:"@Name='\*PCIHDAudioTest\*' and @Resource:Name='PCI3'"** will select test methods PCIHDAudioTest\#4 and PCIHDAudioTest\#5.

Trying out these and other selection queries at the command prompt is left as an exercise for the reader.

 

 





