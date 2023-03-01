import { Component } from '@angular/core';
import { SharedService } from '../shared.service';
import { Router } from '@angular/router';

@Component({
  selector: 'app-admin-home',
  templateUrl: './admin-home.component.html',
  styleUrls: ['./admin-home.component.css']
})
export class AdminHomeComponent {
  constructor (private service:SharedService, private route: Router) {}


  logoutUser(){
    this.service.removeToken();
    this.route.navigate(['']);
  }

}
