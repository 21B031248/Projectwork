import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { FormsModule, ReactiveFormsModule } from '@angular/forms';

import { Observable } from 'rxjs';

@Injectable({
  providedIn: 'root'
})
export class SharedService {

  readonly APIurl = 'http://127.0.0.1:8000/';

  constructor(private http:HttpClient) { }

  getWines():Observable<any[]>{
    return this.http.get<any[]>(this.APIurl + 'wines');
  }

  getCart():Observable<any[]>{
    return this.http.get<any[]>(this.APIurl + 'cart');
  }

  addCartItems(val:any){
    return this.http.post(this.APIurl + 'cart_items', val);
  }

  getCartItems():Observable<any[]>{
    return this.http.get<any[]>(this.APIurl + 'cart_items');
  }

  updateCartItem(val:any){
    return this.http.put(this.APIurl + 'cart_items', val);
  }

  deleteCartItem(val:any){
    return this.http.delete(this.APIurl + 'cart_item/' + val);
  }

  addOrderItem(val:any){
    return this.http.post(this.APIurl + 'cart_items', val);
  }

  getOrder():Observable<any[]>{
    return this.http.get<any[]>(this.APIurl + '/orders/');
  }

}
