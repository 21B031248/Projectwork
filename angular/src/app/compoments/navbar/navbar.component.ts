import { Component, OnInit } from '@angular/core';
import { SharedService } from 'src/app/shared.service';

@Component({
  selector: 'app-navbar',
  templateUrl: './navbar.component.html',
  styleUrls: ['./navbar.component.css']
})
export class NavbarComponent implements OnInit {

  cartId:any=[];

  constructor(private service:SharedService) { }

  ngOnInit(): void {
    this.getCartId();
  }

  getCartId(){
    this.service.getCart().subscribe(data => {
      this.cartId=data;
    });
  }

}
