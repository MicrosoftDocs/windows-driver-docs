---
title: RunAs LowIL
description: TAEF runs the test within a Low Integrity Level process.
ms.assetid: 8FF26AB3-F473-4352-8951-D3F7DF366B5F
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# RunAs LowIL


TAEF runs the test within a Low Integrity Level process.

**Note**  

 

**Note**  On computers running versions of Windows older than Windows Vista, this option is not supported.

 

## <span id="Specifying_RunAs_on_the_Command_Line_"></span><span id="specifying_runas_on_the_command_line_"></span><span id="SPECIFYING_RUNAS_ON_THE_COMMAND_LINE_"></span>Specifying RunAs on the Command Line


``` syntax
te unittests\* /runas:lowil
```

## <span id="Marking_Tests_with_RunAs_"></span><span id="marking_tests_with_runas_"></span><span id="MARKING_TESTS_WITH_RUNAS_"></span>Marking Tests with RunAs


Test metadata can be used to specify the runas type of an assembly, class or test method.

**Note**  RunAs values specified in metadata override RunAs values specified on the command line. For example, a test marked with **runas:system** test metadata will still be run as Local System even if **/runas:elevated** is specified on the command line.

 

Example (native code)

```ManagedCPlusPlus
class MyTests
{
    TEST_CLASS(MyTests);

    BEGIN_TEST_METHOD(LowILTest)
        TEST_METHOD_PROPERTY(L"RunAs", L"LowIL")
    END_TEST_METHOD()
};
```

## <span id="related_topics"></span>Related topics


[RunAs](runas.md)

 

 






