CREATE EXTENSION IF NOT EXISTS "uuid-ossp";
-- public.products definition

-- Drop table

-- DROP TABLE public.products;

CREATE TABLE public.products (
	id serial NOT NULL,
	title varchar NOT NULL,
	price float8 NOT NULL,
	description text NOT NULL,
	category varchar NOT NULL,
	image varchar NULL,
	CONSTRAINT products_pk PRIMARY KEY (id)
);


-- public.users definition

-- Drop table

-- DROP TABLE public.users;

CREATE TABLE public.users (
	id serial NOT NULL,
	email varchar NOT NULL,
	username varchar NOT NULL,
	first_name varchar NOT NULL,
	last_name varchar NOT NULL,
	"password" varchar NOT NULL,
	phone varchar NULL,
	address jsonb NULL,
	document_number varchar NOT NULL,
	CONSTRAINT users_pk PRIMARY KEY (id)
);


-- public.carts definition

-- Drop table

-- DROP TABLE public.carts;

CREATE TABLE public.carts (
	id serial NOT NULL,
	user_id int4 NOT NULL,
	created_at timestamptz NOT NULL DEFAULT now(),
	updated_at timestamptz NULL DEFAULT now(),
	products jsonb NULL,
	CONSTRAINT carts_pk PRIMARY KEY (id),
	CONSTRAINT carts_fk FOREIGN KEY (user_id) REFERENCES public.users(id) ON DELETE RESTRICT ON UPDATE RESTRICT
);


-- public.purchases definition

-- Drop table

-- DROP TABLE public.purchases;

CREATE TABLE public.purchases (
	purchase_id uuid NOT NULL DEFAULT uuid_generate_v4(),
	user_id int4 NOT NULL,
	product_id int4 NOT NULL,
	CONSTRAINT purchases_pk PRIMARY KEY (purchase_id),
	CONSTRAINT purchases_fk FOREIGN KEY (user_id) REFERENCES public.users(id) ON DELETE RESTRICT ON UPDATE RESTRICT,
	CONSTRAINT purchases_fk_1 FOREIGN KEY (product_id) REFERENCES public.products(id) ON DELETE RESTRICT ON UPDATE RESTRICT
);

ALTER TABLE public.purchases ADD "size" varchar NOT NULL;
ALTER TABLE public.purchases ADD color varchar NOT NULL;
ALTER TABLE public.products ADD size_available _text NOT NULL DEFAULT '{S, M, B}';
ALTER TABLE public.products ADD color_available _text NOT NULL DEFAULT '{"black", "red"}';

