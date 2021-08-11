CREATE TABLE public.looks (
    id serial NOT NULL,
    shirt_id int4 NOT NULL,
    jacket_id int4 NULL,
    shoe_id int4 NOT NULL, 
    pant_id int4 NOT NULL,
    description varchar NOT NULL,
    image varchar NULL,
    CONSTRAINT looks_pk PRIMARY KEY (id),
    CONSTRAINT looks_shirt FOREIGN KEY (shirt_id) REFERENCES public.products(id) ON DELETE RESTRICT ON UPDATE RESTRICT,
    CONSTRAINT looks_jacket FOREIGN KEY (jacket_id) REFERENCES public.products(id) ON DELETE RESTRICT ON UPDATE RESTRICT,
    CONSTRAINT looks_shoe FOREIGN KEY (shoe_id) REFERENCES public.products(id) ON DELETE RESTRICT ON UPDATE RESTRICT,
    CONSTRAINT looks_pant FOREIGN KEY (pant_id) REFERENCES public.products(id) ON DELETE RESTRICT ON UPDATE RESTRICT
);