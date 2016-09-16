---
title: RunAs System
description: TAEF runs the test as Local System.
ms.assetid: E1138F36-D043-458A-8424-C649854CB7EE
---

# RunAs System


TAEF runs the test as Local System.

**Note**   The tests that you run as Local System should not create any user interfaces (UI). If your tests need to create or interact with UI, you need to move your UI-related code into separate executables that are launched on a desktop from your tests using [**CreateProcessAsUser function**](https://msdn.microsoft.com/library/windows/desktop/ms682429).

 

## <span id="Specifying_RunAs_on_the_Command_Line_"></span><span id="specifying_runas_on_the_command_line_"></span><span id="SPECIFYING_RUNAS_ON_THE_COMMAND_LINE_"></span>Specifying RunAs on the Command Line


``` syntax
te unittests\* /runas:system
```

## <span id="Marking_Tests_with_RunAs_"></span><span id="marking_tests_with_runas_"></span><span id="MARKING_TESTS_WITH_RUNAS_"></span>Marking Tests with RunAs


Test metadata can be used to specify the runas type of an assembly, class or test method.

**Note**  RunAs values specified in metadata override RunAs values specified on the command line. For example, a test marked with **runas:system** test metadata will still be run as Local System even if **/runas:elevated** is specified on the command line.

 

Example (native code)

```ManagedCPlusPlus
class MyTests
{
    TEST_CLASS(MyTests);

    BEGIN_TEST_METHOD(SystemTest)
        TEST_METHOD_PROPERTY(L"RunAs", L"System")
    END_TEST_METHOD()
};
```

## <span id="related_topics"></span>Related topics


[RunAs](runas.md)

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[taef\taef]:%20RunAs%20System%20%20RELEASE:%20%289/12/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")





