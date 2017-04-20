---
title: RunAs Elevated
description: TAEF ensures that the test is run in an elevated process by spawning an elevated process to run the test if necessary.
ms.assetid: 6292E431-6EB5-4962-BBB0-B86FC4CE4643
ms.author: windows-driver-content
ms.date: 04/20/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# RunAs Elevated


TAEF ensures that the test is run in an elevated process by spawning an elevated process to run the test if necessary.

**Note: The user executing TAEF must be a member of the administrators group in order to execute tests marked with RunAs=Elevated.** This is due to the fact that non-admins do not have a split token to elevate. If a non-admin attempts to run a test which is marked with RunAs=Elevated, **the test will be marked as blocked**.

**Note**  On computers running versions of Windows older than Windows Vista, you must run elevated tests from an administrator process.

 

## <span id="Specifying_RunAs_on_the_Command_Line_"></span><span id="specifying_runas_on_the_command_line_"></span><span id="SPECIFYING_RUNAS_ON_THE_COMMAND_LINE_"></span>Specifying RunAs on the Command Line


``` syntax
te unittests\* /runas:elevated
```

## <span id="Marking_Tests_with_RunAs_"></span><span id="marking_tests_with_runas_"></span><span id="MARKING_TESTS_WITH_RUNAS_"></span>Marking Tests with RunAs


Test metadata can be used to specify the runas type of an assembly, class or test method.

**Note**  RunAs values specified in metadata override RunAs values specified on the command line. For example, a test marked with **runas:system** test metadata will still be run as Local System even if **/runas:elevated** is specified on the command line.

 

Example (native code)

```ManagedCPlusPlus
class MyTests
{
    TEST_CLASS(MyTests);

    BEGIN_TEST_METHOD(ElevatedTest)
        TEST_METHOD_PROPERTY(L"RunAs", L"Elevated")
    END_TEST_METHOD()
};
```

## <span id="related_topics"></span>Related topics


[RunAs](runas.md)

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[taef\taef]:%20RunAs%20Elevated%20%20RELEASE:%20%289/12/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")





