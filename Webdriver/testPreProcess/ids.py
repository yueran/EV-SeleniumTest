# To change this template, choose Tools | Templates
# and open the template in the editor.
#from Webdriver.testPreProcess import createTestUser
#
##gb_testUserId = testUserIdValue
##gb_testUserGroupId = testUserGroupIdValue
##########################################################
#createTestUser.py
userFirstName = "ztestUser"
userLastName = "ztestUser"
userEmailAdd = "ztestUser@test.com"
userName = "ztestUser"
userPassword = "test"
userPasswordRepeat = "test"
userGroupName = "ztestUserGroup"

searchUserFirstName = u"1ab"
searchUserLastName = u"1cd"
searchUserEmailAdd = u"1abcd@abcd.com"
searchUserName = u"1abcd"

editUserFirstName = u"1editUser"
editUserLastName = u"1editUser"
editUserEmailAdd = u"1editUser@test.com"
editUserName = u"1editUser"

duplicateUserGroup = u"1duplicateUserGroup"
editUserGroup = u"2editUserGroup"
#*****************************************************************
#createStuffs.py
ModifyMediaGroup = u"1ModifyMediaGroup"
TestMediaGroup =u"2TestMediaGroup"
#*****************************************************************
#store Hierarchy:
companyTest = u"1companyTest"
storeGroupTest = u"2storeGroupTest"
storeTest = u"3storeTest"
dStore = u"4dStore"
assignStore = u"5assignStore"
#******************************************************************
classifyProductsCategory = u"test"
classifyProductsKeyword = u"keywordOptions"
classfiyProductsSubCategory = u"subCategoryOptions"

#********************************************************************
testProduct1 = u"1testProduct1"
testProduct2 = u"2testProduct2"
testAcc1 = u"3testzAcc1"
testAcc2 = u"4testzAcc2"

#*****************************************************
duplicateTmp = u"1DuplicateTmp"
editTmpSchedule = u"2editTmpSchedule"
modifyTmp = u"3modifyTmp"

#******************************************************
assignLoops = u"1assignLoops"
editLoopSchedule = u"2editLoopSchedule"
editNameOfLoop = u"3editNameOfLoop"

#########################################################
#Update the data here:
#data from createTestUser.py
#Step 1: run createTestUser.py, record the following data; assgin userName to userGroupName;
testUserGroupIdValue="246"
testUserIdValue="245"

#Step 2: Run assignPermissions.py

#Step 3: Run createStoreHierarchy.py, record the following data, assign userGroupName to storeTest;
#data from createStuffs.py
companyTestIdValue="142"
storeGroupTestIdValue="143"
storeTestIdValue="144"
dStoreIdValue="145"
assignStoreIdValue="146"

#Step 4: Run createMedia.py, record the following data.; Assign MediaEditTest.avi to TestMediaGroup
ModifyMediaGroupIdValue= "513"
TestMediaGroupIdValue= "514"
uploadMediaMediumID = "69"

#Step5:Run createCSCKeyWords.py, record the following data:
classifyProductsCategoryIdValue="504"
classifyProductsSubCategoryIdValue="505"
classifyProductsKeywordIdValue="506"

#Step 6: Run createProducts.py, record the following data:
testProduct1IdValue="491"
testProduct2IdValue="492"
testAcc1IdValue="97"
testAcc2IdValue="98"

#Step 7: Run createUsersAndGroups, record the following data:
editUserIdValue="233"
duplicateUserGroupIdValue="234"
editUserGroupIdValue="235"

#Step 8: Run createTemplates,py record the following data:
duplicateTmpIdValue="481"
editTmpScheduleValue="480"
modifyTmpIdValue="482"

#Step 9: Run createLoops.py record the following data:
assignLoopsIdValue="471"
editLoopScheduleIdValue="472"
editNameOfLoopIdValue="473"



