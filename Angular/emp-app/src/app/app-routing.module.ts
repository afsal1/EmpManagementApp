import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { EmployeeComponent } from './employee/employee.component';
import { HomePageComponent } from './home-page/home-page.component';
import { UserLoginComponent } from './user-login/user-login.component';
import { AdminHomeComponent } from './admin-home/admin-home.component';
import { UserSignupComponent } from './user-signup/user-signup.component';

const routes: Routes = [
  {path:'employee',component:EmployeeComponent},
  {path:'',component:UserLoginComponent},
  {path:'home',component:HomePageComponent},
  {path:'admin-home',component:AdminHomeComponent},
  {path:'signup',component:UserSignupComponent}
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
