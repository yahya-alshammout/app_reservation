(function(){
    angular.module("hotelreservation.angapp",[])
    .controller("HotelReservation", ["$scope", HotelReservation])
    .controller("CustomersController", ["$scope", CustomersController])
    .controller("ReservationList", ["$scope", ReservationList]);

    function HotelReservation($scope) {
        $scope.hotels = [
            {hotel_name:"Sheraton", hotel_city:"Dubai"},
            {hotel_name:"Hilton", hotel_city:"Amman"},
        ];
        $scope.add_new_hotel = function(new_hotel, hotels) {
            var hotel = {hotel_name: new_hotel, hotel_city:"Any city"};
            hotels.push(hotel);

        };
    }
    function CustomersController($scope) {
        $scope.customers = [
            {customer_name:"Ahmad", phone_number:"+962782122240"},
            {customer_name:"Mohammad", phone_number:"+962797512450"},
        ];
        $scope.add_new_customer = function(new_customer, customers) {
            var customer = {customer_name: new_customer, phone_number:"+9627712478795"};
            customers.push(customer);
        };
    }
    function ReservationList($scope) {
        $scope.reservations = [
            {reservation_name:"Sheraton", city:"Dubai",enter_hotel:"June 10, 2018, 7a.m", exit_hotel:"June 12, 2018, 7a.m"},
            {reservation_name:"Hilton", city:"Amman",enter_hotel:"April 5, 2018, 9a.m", exit_hotel:"April 10, 2018, 9a.m"},
        ];
        $scope.add_new_reservation = function(new_reservation, reservations) {
            var reservation = {reservation_name: new_reservation, city:"Any city", enter_hotel:"Any time", exit_hotel:"Any time"};
            reservations.push(reservation);
        };
    }
})();