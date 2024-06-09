class Band:
    def __init__(self, name, hometown):
        self._name = None
        self.name = name
        self._hometown = None
        self.hometown = hometown
        self._concerts = []

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if not isinstance(value, str) or len(value) == 0:
            print("Name must be a non-empty string")
        else:
            self._name = value

    @property
    def hometown(self):
        return self._hometown

    @hometown.setter
    def hometown(self, value):
        if self._hometown is not None:
            print("Hometown cannot be changed once set")
        elif not isinstance(value, str) or len(value) == 0:
            print("Hometown must be a non-empty string")
        else:
            self._hometown = value

    #@property
    def concerts(self):
        return self._concerts if self._concerts else None

    #@property
    def venues(self):
        return list(set(concert.venue for concert in self._concerts)) if self._concerts else None

    def add_concert(self, concert):
        self._concerts.append(concert)

    def play_in_venue(self, venue, date):
        return Concert(date, self, venue)

    def all_introductions(self):
        if not self._concerts:
            return None
        return [concert.introduction() for concert in self._concerts]


class Concert:
    all = []
    def __init__(self, date, band, venue):
        self._date = None
        self.date = date
        self._band = None
        self.band = band
        self._venue = None
        self.venue = venue
        Concert.all.append(self)

    @property
    def date(self):
        return self._date

    @date.setter
    def date(self, value):
        if not isinstance(value, str) or len(value) == 0:
            print("Date must be a non-empty string")
        else:
            self._date = value
        

    @property
    def band(self):
        return self._band

    @band.setter
    def band(self, value):
        if not isinstance(value, Band):
            print("Band must be of type Band")
        else:
            if hasattr(self, "_band") and self._band:
                self._band._concerts.remove(self)
            self._band = value
            self._band.add_concert(self)

    @property
    def venue(self):
        return self._venue

    @venue.setter
    def venue(self, value):
        if not isinstance(value, Venue):
            print("Venue must be of type Venue")
        else:
            if hasattr(self, "_venue") and self._venue:
                self._venue._concerts.remove(self)
            self._venue = value
            self._venue.add_concert(self)

    def hometown_show(self):
        return self.band.hometown == self.venue.city

    def introduction(self):
        return f"Hello {self.venue.city}!!!!! We are {self.band.name} and we're from {self.band.hometown}"

class Venue:
    def __init__(self, name, city):
        self._name = None
        self.name = name
        self._city = None
        self.city = city
        self._concerts = []

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if not isinstance(value, str) or len(value) == 0:
            print("Name must be a non-empty string")
        else:
            self._name = value

    @property
    def city(self):
        return self._city

    @city.setter
    def city(self, value):
        if not isinstance(value, str) or len(value) == 0:
            print("City must be a non-empty string")
        else:
            self._city = value

    def add_concert(self, concert):
        self._concerts.append(concert)

    def concerts(self):
        return self._concerts if self._concerts else None

    def bands(self):
        if not self._concerts:
            return None
        return list(set(concert.band for concert in self._concerts))

    def concert_on(self, date):
        for concert in self._concerts:
            if concert.date == date:
                return concert
        return None
