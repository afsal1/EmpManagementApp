import { Component } from '@angular/core';
import { Router } from '@angular/router';
import { SharedService } from 'src/app/shared.service';

@Component({
  selector: 'app-user-login',
  templateUrl: './user-login.component.html',
  styleUrls: ['./user-login.component.css']
})
export class UserLoginComponent {
  constructor(private service:SharedService, private route: Router ) {}


  loginObj: any = {
    email:'',
    password:''
  }

  ngOnInit():void {
   
  }


  onLogin() {
    this.service.onLogin(this.loginObj).subscribe((res:any) => {
      localStorage.setItem('access_token', res.access_token)
      if(res.status == 400){
        alert(res.message.non_field_errors)
        this.route.navigateByUrl('');
      }
      if(res.user_role == 'Admin'){
        this.route.navigateByUrl('/admin-home');
      }else if(res.user_role == 'User'){
        this.route.navigateByUrl('/home');
      }else{
        this.route.navigateByUrl('');
      }
    })
  }

}
