---
title: Execution Groups
description: Execution Groups
ms.assetid: CC196843-A225-4193-9386-EE024B5D0B68
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Execution Groups


Please make sure that you are familiar with basic execution of [TAEF](index.md) and know how to [Author Tests](authoring-tests.md) using it, before proceeding with this section. You might also want to go through some data-driven test example walk-through listed in the User Guide.

## <span id="Scenario-Based_Testing_with_TAEF"></span><span id="scenario-based_testing_with_taef"></span><span id="SCENARIO-BASED_TESTING_WITH_TAEF"></span>Scenario-Based Testing with TAEF


When you talk about scenario-level testing, you are really talking about a series of tests, where the executing the next test makes sense only if the previous test in the scenario succeeded. In some cases, you may not even have all information you need to execute the next test, if the previous test failed. Toward this end, while keeping the unit of execution as a test method and allowing for testing scenarios, TAEF supports what are known as "ExecutionGroup"s. You can have scenario-based tests in TAEF regardless while still having other features like data-driven testing. If you design your scenario to leverage data-driven testing, you can apply data-driven support at class level using Data-driven class functionality offered by TAEF. **By applying data-driven support at class level, you can have all the tests within your class be executed sequentially for each row.**

This page will concentrate on how to specify a sequence of tests within a class as an "ExecutionGroup".

## <span id="Execution_Groups"></span><span id="execution_groups"></span><span id="EXECUTION_GROUPS"></span>Execution Groups


Before discussing Execution Groups, it is important to note and remember that **in TAEF, the order of execution of tests within a class is the order in which you have qualified them as a TEST\_METHOD(...) in case of native code, or added \[TestMethod\] property before the method in case of managed code**. TAEF does not guarantee the order of execution of classes themselves.

**Now, in scenario-based tests, it may not be sufficient to just guarantee the order-of-execution, you also need to guarantee that all previous tests in the scenario succeeded before you proceed to the next test in the scenario.** This is where you will find of concept of "ExecutionGroup" to be useful.

Consider a native example:

```cpp
1     class ExecutionDependencyExample
2     {
3         BEGIN_TEST_CLASS(ExecutionDependencyExample)
4             TEST_CLASS_PROPERTY(L"ExecutionGroup", L"DependentTests")
5         END_TEST_CLASS()
6
7         TEST_METHOD(Test1)
8         {
9             Log::Comment(L"Test1 passes.");
10        }
11
12        TEST_METHOD(Test2)
13        {
14            Log::Comment(L"Test2 fails.");
15            VERIFY_ARE_EQUAL(2, 3);
16        }
17
18        TEST_METHOD(Test3)
19        {
20            Log::Comment(L"Test3 is blocked; so you shouldn&#39;t see this.");
21        }
22    };
```

See line 4 in the C++ file snippet above. In this particular case, you are qualifying all tests within the Class ExecutionDependencyExample to belong to an "ExecutionGroup" called "DependentTests". This means that "Test1", "Test2", and "Test3" are part of the "DependentTests" execution group. As mentioned before, Test2 will get executed if and only if Test1 gets executed successfully and passes. Similarly Test3 will get executed if and only if Test2 gets executed successfully and passes.

You will see that Test2 has been designed to fail (see the lines 14 and 15 above).

Since Test2 fails in our "DependentTests" "ExecutionGroup", Test3 will not get executed and will instead be marked as blocked. Lets try running the above test and see if this is indeed true.

``` syntax
te Examples\CPP.ExecutionDependency.Example.dll
Test Authoring and Execution Framework v2.93k for x86

StartGroup: WEX::TestExecution::Examples::ExecutionDependencyExample::Test1
Test1 passes.
EndGroup: WEX::TestExecution::Examples::ExecutionDependencyExample::Test1 
    [Passed]

StartGroup: WEX::TestExecution::Examples::ExecutionDependencyExample::Test2
Test2 fails.
Error: Verify: AreEqual(2, 3) - Values (2, 3) [File: >f:source\executiondependencyexample\executiondependencyexample.cpp,
Function: WEX::TestExecution::Examples::ExecutionDependencyExample::Test2, Line:21] 
EndGroup: WEX::TestExecution::Examples::ExecutionDependencyExample::Test2[Failed] 

StartGroup: WEX::TestExecution::Examples::ExecutionDependencyExample::Test3
Blocked: This test belongs to an execution group and depends on the previous test being executed in the same environment successfully. The dependent test must be selected for execution, must request the same execution environment (e.g. 'ThreadingModel') and must be executed successfully.
EndGroup: WEX::TestExecution::Examples::ExecutionDependencyExample::Test3 [Blocked]

Non-passing Tests:
    WEX::TestExecution::Examples::ExecutionDependencyExample::Test2 [Failed]
    WEX::TestExecution::Examples::ExecutionDependencyExample::Test3 [Blocked]

Summary: Total=3, Passed=1, Failed=1, Blocked=1, Not Run=0, Skipped=0
```

Notice that, as predicted, Test1 passed, Test2 failed, and Test3 was blocked. With Test3, TAEF logs a message saying that Test3 belongs to an execution group and the previous test did not execute successfully.

This error message also says that all the tests before the current test being executed which belong to the same ExecutionGroup should be selected. In other words, if you try to run only Test2 using a selection criteria at runtime, you will find that Test2 will be blocked as it is execution dependent on Test1, being part of the same ExecutionGroup.

``` syntax
te Examples\CPP.ExecutionDependency.Example.dll /name:*Test2*
Test Authoring and Execution Framework v2.9.3k for x86

StartGroup: WEX::TestExecution::Examples::ExecutionDependencyExample::Test2
Blocked: This test belongs to an execution group and depends on the previous test being executed in the same environment successfully. The dependent test must be selected for execution, must request the same execution environment (e.g. 'ThreadingModel') and must be executed successfully.

EndGroup: WEX::TestExecution::Examples::ExecutionDependencyExample::Test2 [Blocked]

Summary: Total=1, Passed=0, Failed=0, Blocked=1, Not Run=0, Skipped=0
```

If however, you select Test1, which is the first test in the ExecutionGroup, it will run successfully.

``` syntax
te Examples\CPP.ExecutionDependency.Example.dll /name:*Test1*
Test Authoring and Execution Framework v2.9.3k for x86
StartGroup: WEX::TestExecution::Examples::ExecutionDependencyExample::Test1
Test1 passes.
EndGroup: WEX::TestExecution::Examples::ExecutionDependencyExample::Test1 [Passed]

Summary: Total=1, Passed=1, Failed=0, Blocked=0, Not Run=0, Skipped=0
```

Also, if you have tests that do not belong to the ExecutionGroup, they will get executed regardless of the execution outcome of the tests within the ExecutionGroup proceeding them. It is also possible to have more than one ExecutionGroup within a class. Note however that ExecutionGroup cannot span across Classes. If you do so, they will instead be considered as two separate ExecutionGroups, one in each class.

The message also says that Test3 should be run in the same environment as Test2. Lets try to understand this aspect in a little more detail. Since being a part of an ExecutionGroup really means being a part of the scenario-based test, it becomes crucial that all the tests request and hence execute in the same environment. For instance, if the Threading Model changes within an ExecutionGroup, you will see blocked tests. If for example, in the above example, Test2 was designed to execute successfully, but had the 'ThreadingModel' property set to 'MTA', Test3 would still be blocked.

Let's consider another example: Examples\\TAEF\\CSharp\\ExecutionDependentGroupsExample (please refer to the latest TAEF release share)

```cpp
1     [TestClass]
2     public class CSharpExecutionDependentGroupsExample
3     {
4         //First Execution Group: Test1, Test2
5         [TestMethod]
6         [TestProperty("ExecutionGroup", "First Execution Group")]
7         public void Test1()
8         {
9             Log.Comment("Part of First Execution Group");
10        }
11        [TestMethod]
12        [TestProperty("ExecutionGroup", "First Execution Group")]
13        public void Test2()
14        {
15            Log.Comment("Part of First Execution Group");
16        }
17
18        //Second Execution Group: Test3, Test4. Test4 fails
19        [TestMethod]
20        [TestProperty("ExecutionGroup", "Second Execution Group")]
21        public void Test3()
22        {
23            Log.Comment("Part of Second Execution Group");
24        }
25        [TestMethod]
26        [TestProperty("ExecutionGroup", "Second Execution Group")]
27        public void Test4()
28        {
29            Log.Comment("Part of Second Execution Group - last in group fails");
30            Verify.IsTrue(false);
31        }
32
33        //Third Execution Group: Test5, Test6, Test7. Test6 fails, Test7 will be blocked.
34        [TestMethod]
35        [TestProperty("ExecutionGroup", "Third Execution Group")]
36        public void Test5()
37        {
38            Log.Comment("Part of Third Execution Group");
39        }
40        [TestMethod]
41        [TestProperty("ExecutionGroup", "Third Execution Group")]
42        public void Test6()
43        {
44            Log.Comment("Part of Third Execution Group - middle in this set of 3 fails");
45            Verify.IsTrue(false);
46        }
47        [TestMethod]
48        [TestProperty("ExecutionGroup", "Third Execution Group")]
49        public void Test7()
50        {
51            Log.Comment("Part of Third Execution Group");
52        }
53
54        //Fourth Execution Group: Test8, Test9
55        [TestMethod]
56        [TestProperty("ExecutionGroup", "Fourth Execution Group")]
57        public void Test8()
58        {
59            Log.Comment("Part of Fourth Execution Group");
60        }
61        [TestMethod]
62        [TestProperty("ExecutionGroup", "Fourth Execution Group")]
63        public void Test9()
64        {
65            Log.Comment("Part of Fourth Execution Group");
66        }
67    }
```

This example has 4 different execution groups:

-   "First Execution Group" contains Test1, Test2; both of which should pass successfully.
-   "Second Execution Group" contains Test3 and Test4. Test4 is the last test in this ExecutionGroup and it fails.
-   "Third Execution Group" contains Test5, Test6 and Test7. Test5 executes and passes successfully although Test4 from the previous ExecutionGroup failed. Test6 is designed to fail, which will cause Test7 to be Blocked.
-   "Fourth Execution Group" contains Test8 and Test9. Once again, althought Test7 from the previous ExecutionGroup was Blocked due to Test6 failing, Test8 will execute successfully and so will Test9.

Just to understand the ExecutionGroups in this example better, let's list the properties in this example.

``` syntax
te Examples\CSharp.ExecutionDependentGroups.Example.dll /listproperties
Test Authoring and Execution Framework v2.9.3k for x86

        F:\ \Examples\CSharp.ExecutionDependentGroups.Example.dll
            WEX.Examples.CSharpExecutionDependentGroupsExample
                WEX.Examples.CSharpExecutionDependentGroupsExample.Test1
                        Property[ExecutionGroup] = First Execution Group
                WEX.Examples.CSharpExecutionDependentGroupsExample.Test2
                        Property[ExecutionGroup] = First Execution Group

                WEX.Examples.CSharpExecutionDependentGroupsExample.Test3
                        Property[ExecutionGroup] = Second Execution Group
                WEX.Examples.CSharpExecutionDependentGroupsExample.Test4
                        Property[ExecutionGroup] = Second Execution Group

                WEX.Examples.CSharpExecutionDependentGroupsExample.Test5
                        Property[ExecutionGroup] = Third Execution Group
                WEX.Examples.CSharpExecutionDependentGroupsExample.Test6
                        Property[ExecutionGroup] = Third Execution Group
                WEX.Examples.CSharpExecutionDependentGroupsExample.Test7
                        Property[ExecutionGroup] = Third Execution Group

                WEX.Examples.CSharpExecutionDependentGroupsExample.Test8
                        Property[ExecutionGroup] = Fourth Execution Group
                WEX.Examples.CSharpExecutionDependentGroupsExample.Test9
                        Property[ExecutionGroup] = Fourth Execution Group
```

When you execute the test above, the following output confirms the predicted execution order.

``` syntax
te Examples\CSharp.ExecutionDependentGroups.Example.dll
Test Authoring and Execution Framework v2.9.3k for x86

StartGroup: WEX.Examples.CSharpExecutionDependentGroupsExample.Test1

Part of First Execution Group
EndGroup: WEX.Examples.CSharpExecutionDependentGroupsExample.Test1 [Passed]
StartGroup: WEX.Examples.CSharpExecutionDependentGroupsExample.Test2

Part of First Execution Group
EndGroup: WEX.Examples.CSharpExecutionDependentGroupsExample.Test2 [Passed]

StartGroup: WEX.Examples.CSharpExecutionDependentGroupsExample.Test3

Part of Second Execution Group
EndGroup: WEX.Examples.CSharpExecutionDependentGroupsExample.Test3 [Passed]
StartGroup: WEX.Examples.CSharpExecutionDependentGroupsExample.Test4

Part of Second Execution Group - last in group fails
Error: Verify: IsTrue [File: Need_Symbols, Function: Test4, Line: 0] 
Error: [HRESULT: 0x80131604]. Operation failed: 'WEX.Examples.CSharpExecutionDependentGroupsExample.Test4'.
EndGroup: WEX.Examples.CSharpExecutionDependentGroupsExample.Test4 [Failed]

StartGroup: WEX.Examples.CSharpExecutionDependentGroupsExample.Test5

Part of Third Execution Group
EndGroup: WEX.Examples.CSharpExecutionDependentGroupsExample.Test5 [Passed]
StartGroup: WEX.Examples.CSharpExecutionDependentGroupsExample.Test6

Part of Third Execution Group - middle in this set of 3 fails
Error: Verify: IsTrue [File: Need_Symbols, Function: Test6, Line: 0] 
Error: [HRESULT: 0x80131604]. Operation failed: 'WEX.Examples.CSharpExecutionDependentGroupsExample.Test6'.
EndGroup: WEX.Examples.CSharpExecutionDependentGroupsExample.Test6 [Failed] 
Error: WEX.Examples.CSharpExecutionDependentGroupsExample.Test7 belongs to an execution group and depends
       on the previous test being executed in the same environment successfully.
Error: Please make sure that the dependent test is selected for execution, requests the same execution .
       environment metadata(e.g. 'ThreadingModel') and that it executed successfully.
StartGroup: WEX.Examples.CSharpExecutionDependentGroupsExample.Test7
Blocked EndGroup: WEX.Examples.CSharpExecutionDependentGroupsExample.Test7 [Blocked]

StartGroup: WEX.Examples.CSharpExecutionDependentGroupsExample.Test8

Part of Fourth Execution Group
EndGroup: WEX.Examples.CSharpExecutionDependentGroupsExample.Test8 [Passed]
StartGroup: WEX.Examples.CSharpExecutionDependentGroupsExample.Test9

Part of Fourth Execution Group
EndGroup: WEX.Examples.CSharpExecutionDependentGroupsExample.Test9 [Passed]

Failed Tests:
    WEX.Examples.CSharpExecutionDependentGroupsExample.Test4
    WEX.Examples.CSharpExecutionDependentGroupsExample.Test6

Summary: Total=9, Passed=6, Failed=2, Blocked=1, Not Run=0, Skipped=0
```

Notice that the test execution order is as expected.

 

 





