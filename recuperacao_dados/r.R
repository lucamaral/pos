# install.packages("tidyverse")

library(tidyverse)


#mpg2 <- transmute(mpg,
#  manufacturer = manufacturer,
  #model = model,
  #year = year,
  #
#)

View(mpg)

mpg_ <- select(mpg, year, model, manufacturer)

View(mpg_)

# fazer tipo pipe do bash
# %>% => operador do pipe
mpg %>%
  select (
    year, model
  ) %>%
  View

# preview das infos
?mpg

# ordenacao
mpg %>%
  select (
    year, model
  ) %>%
  arrange(-year) %>%
  View

mpg %>%
  count(manufacturer) %>%
  arrange(n)

?arrange

mpg %>%
  count(manufacturer, year) %>%
  arrange(n)

mpg %>%
  count(manufacturer, year) %>%
  arrange(n) %>%
  spread(year, n) %>%
   View()

?spread

?mpg

# sumarizar, criar nova coluna com diferença, filtrar

mpg %>%
  group_by(manufacturer, year) %>%
  summarise(
    media_cidade = mean(cty),
    media_via = mean(hwy)
  ) %>%
  mutate (
    diff_media = media_via - media_cidade,
    
  ) %>%
  arrange(diff_media) %>%
  filter(
    media_cidade > 20,
    media_cidade < 24
  ) %>%
  View()

mpg %>%
  ggplot(aes(x = manufacturer)) + 
  geom_bar() + 
  coord_flip()

mpg %>%
  group_by(manufacturer) %>%
  summarise(
    media_cidade = mean(cty)
  ) %>%
  ggplot(aes(x = manufacturer, y = media_cidade)) +
  geom_bar(stat = "identity") + 
  coord_flip() +
  labs(
    x = "Fabricante",
    y = "Média",
    title = "Consumo médio por fabricante"
  )

?geom_bar

?right_join

colnames(mpg)

?mpg

ggplot(mpg, aes(x = cty)) +
  geom_histogram(aes(color = drv), fill = 'identify', bins = 30)

mpg %>%
  ggplot(aes(cty)) +
  geom_histogram(bins = 30) +
  facet_wrap(~drv)

?mpg

mpg %>%
  ggplot(aes(cty)) +
  geom_histogram(bins = 30) +
  facet_grid(fl ~drv)

mpg %>%
  ggplot(aes(cty)) +
  geom_density(bins = 30) +
  facet_grid(fl ~drv)

mpg %>%
  ggplot(aes(displ, cty)) +
  geom_point(alpha=0.1) +
  geom_smooth()

mpg %>%
  ggplot(aes(displ, cty)) +
  geom_point(aes(color = drv), alpha=0.1) +
  geom_smooth(se = FALSE)

mpg %>%
  ggplot(aes(displ, cty)) +
  geom_point(aes(color = drv), alpha=0.1) +
  geom_smooth(se = FALSE) +
  facet_wrap(~drv)

modelo <- lm(
  cty ~ displ,
  mpg
)

modelo$coefficients

library(modelr)

mpg <- mpg %>%
  add_predictions(modelo)

mpg$pred

mpg %>%
  ggplot(aes(displ)) +
  geom_point(aes(y = cty), color = "red") +
  geom_point(aes(y = pred), color = "blue")

?mpg

mpg <- mpg %>%
    add_residuals(modelo)

mpg %>%
   ggplot(aes(cty, resid)) +
  geom_point(aes(color = drv))
 