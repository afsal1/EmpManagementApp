import { Component } from '@angular/core';
import { Router } from '@angular/router';
import { SharedService } from 'src/app/shared.service';

@Component({
  selector: 'app-user-signup',
  templateUrl: './user-signup.component.html',
  styleUrls: ['./user-signup.component.css']
})
export class UserSignupComponent {

  constructor(private service:SharedService, private route: Router ) {}

  signupUsers: any[] = [];

  signupObj: any = {
    first_name:'',
    last_name:'',
    email:'',
    password:'',
    user_role:''
  };

  ngOnInit():void {
    this.signupObj.first_name = this.signupObj.first_name;
    this.signupObj.last_name = this.signupObj.last_name;
    this.signupObj.email = this.signupObj.email;
    this.signupObj.user_role = this.signupObj.user_role;
    this.signupObj.password = this.signupObj.password;
  }

  onSignup() {
    var val = {first_name:this.signupObj.first_name,
      last_name:this.signupObj.last_name,
      user_role:this.signupObj.user_role,
      email:this.signupObj.email,
      password:this.signupObj.password
    };
    this.service.onSignup(val).subscribe((res:any)=>{

      if(res.status == "400"){
        alert(res.message.non_field_errors);
        this.route.navigateByUrl('signup');
      }
      else if(res.status == "200"){
        alert('you are successfully registered')
        this.route.navigateByUrl('');
      }
      else{
        alert('email already exists')
        this.route.navigateByUrl('signup');
      }
    })
  }
}
